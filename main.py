from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Set up window
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Classic Snake Game')
screen.bgcolor('khaki')

# Instantiate snake, food & score
snake = Snake()
food = Food()
score = Score()

# Set up snake's movements
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# Game
is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move() # Animation config

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh() # Gives new location to food object
        snake.extend() # Extends snake
        score.add_score() # Adds 1 and updates score

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = False
        score.game_over()

    # Detect collision with tail/body
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()










screen.exitonclick()