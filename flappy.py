import pygame
import random
import sys
import neat

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAVITY = 0.25
FLAP_HEIGHT = -8
PIPE_WIDTH = 50
PIPE_SPEED = 3
PIPE_GAP = 200
FPS = 60

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 36)

# Classes
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.radius = 20
        self.alive = True

    def flap(self):
        self.velocity = FLAP_HEIGHT

    def update(self):
        if self.alive:
            self.velocity += GRAVITY
            self.y += self.velocity

            # Keep bird within screen bounds
            if self.y > SCREEN_HEIGHT:
                self.y = SCREEN_HEIGHT
                self.velocity = 0
            if self.y < 0:
                self.y = 0
                self.velocity = 0

    def show(self, screen):
        pygame.draw.circle(screen, RED, (self.x, int(self.y)), self.radius)


class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.gap = PIPE_GAP
        self.top = random.randint(50, SCREEN_HEIGHT - self.gap - 50)
        self.bottom = self.top + self.gap

    def show(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, 0, PIPE_WIDTH, self.top))
        pygame.draw.rect(screen, BLACK, (self.x, self.bottom, PIPE_WIDTH, SCREEN_HEIGHT - self.bottom))

    def update(self):
        self.x -= PIPE_SPEED

    def offscreen(self):
        return self.x < -PIPE_WIDTH

    def hits(self, bird):
        if bird.y - bird.radius < self.top or bird.y + bird.radius > self.bottom:
            if self.x < bird.x < self.x + PIPE_WIDTH:
                return True
        return False


# NEAT Configurations
def eval_genomes(genomes, config):
    global SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_WIDTH, PIPE_SPEED, PIPE_GAP

    nets = []
    ge = []
    birds = []

    for genome_id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird())
        g.fitness = 0
        ge.append(g)

    pipes = []

    score = 0
    high_score = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Generate new pipes
        if len(pipes) == 0 or pipes[-1].x < SCREEN_WIDTH - 150:
            pipes.append(Pipe())

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + PIPE_WIDTH:
                pipe_ind = 1

        for x, bird in enumerate(birds):
            ge[x].fitness += 0.1
            bird.update()

            # AI controls
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].top), abs(bird.y - pipes[pipe_ind].bottom)))
            if output[0] > 0.5:
                bird.flap()

            # Check collisions
            for pipe in pipes:
                if pipe.hits(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

            # Remove pipes that go offscreen
            if pipes and pipes[0].offscreen():
                pipes.pop(0)
                score += 1

            # Remove birds that go offscreen or collide with pipes
            if bird.y >= SCREEN_HEIGHT or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        # # Draw everything
        # screen.fill(WHITE)
        # for bird in birds:
        #     bird.show(screen)
        # for pipe in pipes:
        #     pipe.show(screen)

        # # Display score
        # score_text = FONT.render(f'Score: {score}', True, BLACK)
        # screen.blit(score_text, (10, 10))

        # high_score_text = FONT.render(f'High Score: {high_score}', True, BLACK)
        # screen.blit(high_score_text, (10, 50))

        # pygame.display.update()
        # clock.tick(FPS)


def run_neat(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 50)


# Main function
def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird AI')

    config_path = "neat_config.txt"
    run_neat(config_path)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
