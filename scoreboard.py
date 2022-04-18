from turtle import Turtle

# Score customization constants
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class Score(Turtle):
    """
    Score starts at 0.
    Function that keeps track of the score and displays it on the screen. Increments score by 1 every time the snake collides with food.
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(-250, 275)
        self.score = 0
        self.track_score()


    def track_score(self):
        """
        Returns updated score.
        """
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)


    def add_score(self):
        """
        Increments score by 1.
        """
        self.score +=1
        self.clear()
        self.track_score()

    def game_over(self):
        """
        Writes 'Game Over' on the centre of screen.
        """
        self.clear()
        self.goto(0, 0)
        self.write(f'  GAME OVER\nTotal score: {self.score}', align=ALIGNMENT, font=FONT)