from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        file = open("high_score.txt")
        high_score = int(file.read())
        file.close()
        return high_score

    def save_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
