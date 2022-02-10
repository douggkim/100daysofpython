import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
car_list = []
game_is_on = True
turtle_generation_counter = 0
while game_is_on:
    time.sleep(0.1)
    # scoreboard.failure()
    screen.update()

    if player.reached_goal():
        scoreboard.success()
        CarManager().increase_speed()
        for car in car_list:
            car.remove_car()
    if turtle_generation_counter % 5 == 0:
        car_list.append(CarManager())
        turtle_generation_counter = 0
    for car in car_list:
        car.move()
        if car.distance(player) < 20:
            scoreboard.failure()
            scoreboard.update_level()
            player.game_over()
            for car in car_list:
                car.remove_car()
            time.sleep(4)
            turtle_generation_counter = 0

    turtle_generation_counter += 1

screen.exitonclick()
