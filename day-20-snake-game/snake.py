from turtle import Turtle
MOVE_DISTANCE = 20
DIRECTIONS = {
    'up': 90,
    "down": 270,
    "left": 180,
    "right": 0
}

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            self.add_segment((x_pos,0))
            x_pos -= MOVE_DISTANCE
    
    def add_segment(self, position):
        square = Turtle("square")
        square.speed("fastest")
        square.color("#7FFF00")
        square.penup()
        square.goto(position)
        self.segments.append(square)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor())    
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DIRECTIONS['down']:
            self.head.setheading(DIRECTIONS['up'])    

    def down(self):
        if self.head.heading() != DIRECTIONS['up']:
            self.head.setheading(DIRECTIONS['down']) 

    def left(self):
        if self.head.heading() != DIRECTIONS['right']:
            self.head.setheading(DIRECTIONS['left'])  

    def right(self):
        if self.head.heading() != DIRECTIONS['left']:
            self.head.setheading(DIRECTIONS['right']) 

