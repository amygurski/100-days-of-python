from turtle import Turtle
MOVEMENT = 20

class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(start_position)
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT)
    
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT)
