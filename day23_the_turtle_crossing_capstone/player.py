from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.left(90)
        self.setpos(STARTING_POSITION[0], STARTING_POSITION[1])

    def move_up(self):
        self.setpos(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reached_goal(self):
        if self.ycor() >= 280:
            self.setpos(STARTING_POSITION[0], STARTING_POSITION[1])
            return True

    def game_over(self):
        self.setpos(STARTING_POSITION[0], STARTING_POSITION[1])
