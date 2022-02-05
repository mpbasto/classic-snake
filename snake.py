from turtle import Turtle

# Position and orientation constants
INITIAL_POSITIONS = [0, -20, -40]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.build_snake()
        self.head = self.body[0]

    def build_snake(self):
        """Creates default snake object."""
        for position in INITIAL_POSITIONS:
            body_part = Turtle('square')
            body_part.color('sea green')
            body_part.penup()
            body_part.setx(position)
            self.body.append(body_part)

    def move(self):
        """Configures snake's animation."""
        for parts in range(len(self.body) - 1, 0, -1):
            new_x = self.body[parts - 1].xcor()
            new_y = self.body[parts - 1].ycor()
            self.body[parts].goto(new_x, new_y)
        self.head.forward(STEP)

    def up(self):
        """Sets snake's orientation to a 90º angle in relation to screen."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets snake's orientation to a 270º angle in relation to screen."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets snake's orientation to a 180º angle in relation to screen."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets snake's orientation to a 0º angle in relation to screen."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)