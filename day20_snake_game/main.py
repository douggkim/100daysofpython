from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import scoreboard
import time

# create a snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # 개별 animation 을 끔

snake = Snake()
food = Food()
scoreboard = scoreboard()

snake.create_snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving snakes
game_is_on = True
scoreboard.write_score()
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


     # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.write_score()
        snake.extend()

    # detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() <-280 \
    or snake.segments[0].ycor() >280 or snake.segments[0].ycor() <-280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
