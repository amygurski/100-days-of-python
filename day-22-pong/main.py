from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HORIZONTAL_EDGE = (SCREEN_WIDTH / 2) - 20

SCREEN_HEIGHT = 600
SCREEN_VERTICAL_EDGE = (SCREEN_HEIGHT / 2) - 20

PADDLE_POSITION = (SCREEN_WIDTH / 2)-50
PADDLE_BALL_CONTACT = (SCREEN_WIDTH / 2) - 80

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((PADDLE_POSITION,0))
left_paddle = Paddle((-PADDLE_POSITION,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > SCREEN_VERTICAL_EDGE or ball.ycor() < -SCREEN_VERTICAL_EDGE:
        ball.bounce_y()

    # Detect collision with paddle 
    if (ball.distance(right_paddle) < 50 and ball.xcor() > PADDLE_BALL_CONTACT) or (ball.distance(left_paddle) < 50 and ball.xcor() < -PADDLE_BALL_CONTACT):
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect Right paddle miss
    if ball.xcor() > SCREEN_HORIZONTAL_EDGE:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect Left paddle miss
    if ball.xcor() < -SCREEN_HORIZONTAL_EDGE:
        ball.reset_position()
        scoreboard.r_point()
    
    # End game when someone has 5 points
    if scoreboard.l_score >= 5 or scoreboard.r_score >= 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()