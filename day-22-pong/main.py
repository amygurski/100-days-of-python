from turtle import Turtle, Screen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_POSITION = (SCREEN_WIDTH/2)-50

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((PADDLE_POSITION,0))
left_paddle = Paddle((-PADDLE_POSITION,0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()