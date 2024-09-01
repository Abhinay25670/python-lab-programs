import turtle

win = turtle.Turtle()
turtle.title("Square")
turtle.bgcolor("black")
win.pensize(8)
win.color("cyan")
win.speed(1)
win.hideturtle()
win.penup()
win.setposition(-50,50)
win.pendown()
for i in range(4):
    win.forward(100)
    win.right(90)
turtle.exitonclick()