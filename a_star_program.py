#A* program

import heapq


class State:

    def __init__(self, word, cost, path):
        self.word, self.cost, self.path = word, cost, path

    def __lt__(self, other):
        return self.cost < other.cost


def generate_permutations(start, goal):
    open_list, closed = [], set()
    start_state = State(start, 0, [start])
    heapq.heappush(open_list, start_state)

    while open_list:
        current = heapq.heappop(open_list)

        if current.word == goal:
            return current.path

        closed.add(current.word)

        for i in range(len(current.word)):
            for j in range(i + 1, len(current.word)):
                new_word = current.word[:i] + current.word[j] + current.word[
                    i + 1:j] + current.word[i] + current.word[j + 1:]

                if new_word not in closed:
                    new_cost = len(goal) - sum(a == b
                                               for a, b in zip(new_word, goal))
                    new_state = State(new_word, new_cost,
                                      current.path + [new_word])
                    heapq.heappush(open_list, new_state)

    return None


initial, goal = "hello", "olleh"
result = generate_permutations(initial, goal)

if result:
    print("Permutations:")
    for idx, perm in enumerate(result):
        print(f"{idx}: {perm}")
else:
    print("No path found.")
