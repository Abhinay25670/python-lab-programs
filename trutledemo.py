import turtle


turtle.title("hello Turtle")
t= turtle.Turtle()
t.color("cyan")
turtle.bgcolor("red")
t.shape("turtle")
t.begin_fill()
t.forward(150)
t.left(72)
t.forward(150)
t.left(72)
t.forward(150)
t.left(72)
t.forward(150)
t.left(72)
t.forward(150)
t.end_fill()

t.penup()
t.goto(-300,50)
t.pendown()
t.pen(pencolor="yellow",fillcolor="red",speed=10)
t.circle(100)
t.hideturtle()

turtle.exitonclick()