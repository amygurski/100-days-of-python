from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)

def take_start_positions():
    all_turtles = []
    y_pos = -125
    for color in COLORS:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        all_turtles.append(new_turtle)
        new_turtle.penup()
        new_turtle.goto(x=-230,y=y_pos)
        y_pos += 50
    return all_turtles

is_race_on = False

all_turtles = take_start_positions()

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"Sorry, you've lost! The {winning_color} turtle is the winner.")
        turtle.forward(random.randint(10,20))

screen.exitonclick()
