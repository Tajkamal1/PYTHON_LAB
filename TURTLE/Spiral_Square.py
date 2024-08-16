import turtle 

wn=turtle.Screen()

wn.bgcolor("yellow")

skk=turtle.Turtle()
skk.speed(0)

skk.color("blue")

def sqrfunc(size):
    for i in range (4):
        skk.fd(size)
        skk.left(90)
        size=size+5

s=6
for i in range(10):
    sqrfunc(s)
    s=s+20

skk.hideturtle()
    
turtle.done()
