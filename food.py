from turtle import Turtle
import random


class Food(Turtle):
    """
    Renders itself as a small dot on the screen. Food will move to a new random location everytime the snake eats it.
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        """ Creates random x & y locations to move Food within a 280 x 280 matrix."""
        random_x =random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
