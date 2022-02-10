from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_level()

    def failure(self):
        self.level = 0
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=("Verdana", 20, "normal"))
        time.sleep(3)
        self.clear()

    def success(self):
        self.clear()
        self.level += 1
        self.update_level()

    def update_level(self):
        self.setpos(-280, 280)
        self.write(f"Level : {self.level}", align="left", font=("Verdana", 10, "normal"))
