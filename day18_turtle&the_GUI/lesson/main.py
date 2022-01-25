from turtle import *
import random

color_set = ["IndianRed", "LightCoral", "Salmon", "DarkSalmon", "LightSalmon"]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

for _ in range(0, 4):
    timmy.forward(100)
    timmy.right(90)


def draw_dotted():
    for _ in range(0, 10):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


def draw_polygon(lines, length, color):
    timmy.color(color)
    each_angle = 360 / lines
    for _ in range(0, lines):
        timmy.forward(length)
        timmy.right(each_angle)


for _ in range(3, 10):
    draw_polygon(_, 50, "green")


def random_walk(line_size, pen_size, speed):
    timmy.speed(speed)
    timmy.pensize(pen_size)
    timmy.dot(15, "Black")
    timmy.color(random.choice(color_set))
    timmy.forward(line_size)
    timmy.right(random.randint(1, 4) * 90)


for _ in range(0, 100):
    random_walk(40, 10, "fastest")


def random_walk(line_size, pen_size, speed):
    timmy.speed(speed)
    timmy.pensize(pen_size)
    timmy.dot(15, "Black")
    timmy.color(random.choice(color_set))
    timmy.forward(line_size)
    timmy.right(random.randint(1, 4) * 90)


for _ in range(0, 100):
    random_walk(40, 10, "fastest")

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph():
    timmy.speed("fastest")
    for _ in range(1, 361):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(1)


def draw_spirograph_heading(spacing):
    timmy.speed("fastest")
    for _ in range(1, 361, spacing):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + spacing)
