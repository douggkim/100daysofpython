from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.reset_num = 0
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.setpos(new_x, new_y)

    def bounce_upper_lower(self):
        self.move_y = self.move_y*-1.1
        self.move_x = self.move_x * 1.1

    def bounce_left_right(self):
        self.move_x = self.move_x*-1.1
        self.move_y = self.move_y * 1.1

    def ball_reset(self):
        # self.angle = random.randint(180, 359)

        if self.xcor() > 385:
            self.move_x = -10
            self.move_y = 10
        elif self.xcor() < -380:
            self.move_x = 10
            self.move_y = 10

        self.setpos(0, 0)

