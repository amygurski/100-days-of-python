from random import choice
from turtle import Turtle, Screen

COLORS = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def draw_row():
    for _ in range(10):
        turtle.dot(20, choice(COLORS))
        turtle.forward(50)

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")

y = 50
for _ in range(10):
    draw_row()
    turtle.setpos(0,y)
    y += 50

screen.exitonclick()