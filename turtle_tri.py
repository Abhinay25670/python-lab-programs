import turtle

win = turtle.Turtle()
turtle.title("triangle")
turtle.bgcolor("black")
win.color("sky blue")
win.hideturtle()
win.speed(1)
win.pensize(8)
win.penup()
win.setposition(-50,50)
win.pendown()
for i in range(3):
    win.forward(100)
    win.left(120)
turtle.exitonclick()