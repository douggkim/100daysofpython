from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()

# # create paddle & Ball
ball = Ball()

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))

screen.update()
# move paddle
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")
screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_upper_lower()

    # detect the collision with r_paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 320:
        ball.bounce_left_right()

    if ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_left_right()

    if ball.xcor() > 385:
        ball.ball_reset()
        scoreboard.left_won()

    if ball.xcor() < -385:
        ball.ball_reset()
        scoreboard.right_won()

screen.exitonclick()
