from turtle import Screen
from snake import Snake
import time

# Set up window
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Classic Snake Game')
screen.bgcolor('khaki')

# Instantiate snake
snake = Snake()

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

    snake.move()


















screen.exitonclick()