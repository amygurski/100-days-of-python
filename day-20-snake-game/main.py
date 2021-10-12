from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE = 600
SCREEN_EDGE = SCREEN_SIZE * 0.45

# Setup screen
screen = Screen()
screen.setup(width=SCREEN_SIZE,height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.register_shape("teeny_apple.gif")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:     
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.move()
        snake.extend()
    
    # Detect collision with wall
    if snake.head.xcor() > SCREEN_EDGE or snake.head.xcor() < -SCREEN_EDGE or snake.head.ycor() > SCREEN_EDGE or snake.head.ycor() < -SCREEN_EDGE:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()