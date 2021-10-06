from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_counterclockwise():
    tim.left(5)

def turn_clockwise():
    tim.right(5)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

MOVEMENTS = {
    "w": move_forwards,
    "s": move_backwards,
    "a": turn_counterclockwise,
    "d": turn_clockwise,
    "c": clear_drawing
}

screen.listen()
for k,v in MOVEMENTS.items():
    screen.onkey(key=k, fun=v)

screen.exitonclick()
