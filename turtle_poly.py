import turtle

win = turtle.Turtle()
turtle.title("Polygon")
turtle.bgcolor("black")

win.hideturtle()
win.pensize(8)
win.penup()
win.setposition(-50,50)
win.pendown()
win.speed(5)
l1=["sky blue","red","purple","white","yellow","pink","orange","green"]
for i in range(8):
    win.color(l1[i])
    win.forward(100)
    win.right(45)

win.penup()
win.setposition(-10,10)
win.pendown()
win.pensize(8)
l1=["sky blue","red","purple","white","yellow","pink","orange","green"]
for i in range(8):
    win.color(l1[i])
    win.forward(100)
    win.right(45)


turtle.exitonclick()