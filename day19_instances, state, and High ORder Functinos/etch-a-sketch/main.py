from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(5)

def turn_counter_clockwise():
    tim.left(5)

def clear():
    tim.setposition(0,0)
    tim.clear()


screen.listen()
# fun 뒤에는 () 를 붙이지 않는다. function 을 인수로 넣을 때는 추가하지 않음.
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()