from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# fun 뒤에는 () 를 붙이지 않는다. function 을 인수로 넣을 때는 추가하지 않음.
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()