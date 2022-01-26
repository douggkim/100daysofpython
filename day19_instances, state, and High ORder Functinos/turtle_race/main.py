from turtle import Turtle, Screen 
import random
# declaration of turtle and screen 
screen = Screen() 

# screen setup 
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make Your Bet", prompt = "Which turtle will win the race? Enter a color : ")


# turtle setup
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

for i in range(len(colors)):
    test_turtle = Turtle(shape = "turtle")
    test_turtle.penup()
    test_turtle.color(colors[i])
    test_turtle.goto( x = -230, y = - 100 + i*200/6)
    turtle_list.append(test_turtle)

if user_bet:
    is_race_on = True

while is_race_on :

    for turtle in turtle_list:
        if turtle.xcor() > 230 : 
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner ! ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner ! ")
        turtle.forward(random.randint(0,10))



screen.exitonclick()
