import turtle
turtle.title("conditional turtle")
turtle.bgcolor("light pink")
t = turtle.Turtle()
t.color("green")

res = input("enter yes or no:")

if res == "yes":
    t.circle(90)
else:
    print("unable to draw enter yes")
t.hideturtle()

turtle.exitonclick()