from turtle import Turtle, Screen

UP = 20
DOWN = 20

class Paddle(Turtle):
    # create paddle
    def __init__(self, pos_tuple):
        super().__init__()
        screen = Screen()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        # set position
        self.setpos(pos_tuple[0], pos_tuple[1])


    # move paddle - predefined function
    def up(self):
        self.sety(self.ycor() + UP)

    def down(self):
        self.sety(self.ycor() - DOWN)
