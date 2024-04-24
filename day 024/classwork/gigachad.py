from turtle import *

speed(30)
width(7)

def draw_square():
    for i in range(4):
        forward(200)
        left(90)

draw_square()

penup()
goto(-300,-300)
pendown()

draw_square()

penup()
goto(0,-300)
pendown()

draw_square()

penup()
goto(-300,0)
pendown()

draw_square()

exitonclick()