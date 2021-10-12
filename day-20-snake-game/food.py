from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("teeny_apple.gif")
        self.speed("fastest")
        self.goto(random.randint(-280,280), random.randint(-280,280))

    def move(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))
