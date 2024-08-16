import turtle
loadWindow = turtle.Screen()
loadWindow.bgcolor("black")

turtle.speed(0)
turtle.pencolor("yellow")

for i in range(40):
    turtle.circle(2*i)
    turtle.circle(-2*i)
    turtle.left(i)

turtle.exitonclick()
