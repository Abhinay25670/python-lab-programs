import turtle

win = turtle.Turtle()

turtle.title("W")
turtle.bgcolor("black")

win.speed(1)
win.hideturtle()
win.pensize(8)
win.color("sky blue")

win.penup()
win.setposition(-50,50)
win.pendown()

win.right(75)
win.forward(100)
win.left(150)
win.forward(100)
win.right(150)
win.forward(100)
win.left(150)
win.forward(100)
turtle.exitonclick()