import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.setpos(280, random.randint(-250, 250))
        self.move_num = STARTING_MOVE_DISTANCE

    def increase_speed(self):
        self.move_num += MOVE_INCREMENT

    def move(self):
        self.setpos(self.xcor() - self.move_num, self.ycor())
        if self.xcor() < -270:
            self.reset()

    def remove_car(self):
        self.reset()
