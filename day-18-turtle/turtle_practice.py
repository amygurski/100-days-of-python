from turtle import Turtle, Screen
from random import randint, choice, randrange

tim = Turtle()

def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)

def draw_dashed_line():
    for _ in range(15):
        tim.up()
        tim.forward(10)
        tim.down()
        tim.forward(10)

def draw_shape(num_sides):
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(360 / num_of_sides)

def get_random_turtle_color():
    screen.colormode(255)
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    tim.pencolor(random_color)

def make_random_movement():
    tim.forward(randrange(10,100))
    tim.setheading(choice([90,180,270,360]))

def draw_spirograph(step_size):
    for _ in range(int(360 / step_size)):
        get_random_turtle_color()
        tim.circle(100)
        tim.setheading(tim.heading() + step_size)

screen = Screen()

# draw_square()
# draw_dashed_line()

# Draw from triangle to decagon
# for num_of_sides in range(3,11):
#     get_random_turtle_color()
#     draw_shape(num_of_sides)

# Draw a random walk
# tim.pensize(15)
# tim.speed('fastest')
# for _ in range(100):
#     get_random_turtle_color()
#     make_random_movement()

# Make a spirograph
tim.speed('fastest')
draw_spirograph(5)

screen.exitonclick()

