from turtle import Turtle

# Position and orientation constants
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Creates a new snake object (3 sea green-colored squares) whenever a Snake object is created.

    - .build_snake(): builds default snake object
    - .move(): configures the snake's animation
    - .up(): sets snake's orientation to a 90º angle in relation to screen
    - .down(): sets snake's orientation to a 270º angle in relation to screen
    - .left(): sets snake's orientation to a 180º angle in relation to screen
    - .right(): sets snake's orientation to a 0º angle in relation to screen

    """

    def __init__(self):
        self.body = []
        self.build_snake()
        self.head = self.body[0]

    def build_snake(self):
        """Creates default snake object."""
        for position in INITIAL_POSITIONS:
            self.segment(position)


    def segment(self, position):
        """Creates segment for snake object"""
        body_part = Turtle('square')
        body_part.color('sea green')
        body_part.penup()
        body_part.goto(position)
        body_part.speed('fastest')
        self.body.append(body_part)


    def extend(self):
        """Adds a new segment to snake object."""
        self.segment(self.body[-1].position()) # gets last segment's position and adds extra segment

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