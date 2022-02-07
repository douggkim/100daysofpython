from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.high_score = 0
        self.update_highscore()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    # reade file 하면 읽은 데이터는 이미 읽은 걸로 바뀜.
    def update_highscore(self):
        if os.path.isfile("data.txt"):
            with open("data.txt", mode="r") as file:
                text_highscore = file.read()
                int_highscore = int(text_highscore)
                self.high_score = int_highscore
        else:
            self.high_score = 0
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as scorefile:
                scorefile.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()