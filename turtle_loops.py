import turtle

turtle.title("Loops in turtle")
turtle.bgcolor("black")
t= turtle.Turtle()
t.pensize(8)

colors=["red","purple","pink","blue","white","green","orange","brown"]
for i in range(8):
    t.color(colors[i])
    t.fd(100)
    t.lt(45)

t.hideturtle()
turtle.exitonclick()