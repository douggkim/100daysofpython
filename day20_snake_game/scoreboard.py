from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=275)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Verdana", 8, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=("Verdana", 8, "normal"))