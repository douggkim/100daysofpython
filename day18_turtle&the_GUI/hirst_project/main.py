from turtle import *
import colorgram
import random

# colorgram으로 input 이미지에서 색 추출
color_set = colorgram.extract("color_picture.jpg", 50)
color_set_rgb = []

# colorgram의 결과값은 class 이며 rgb 멤버 변수를 추출함
for _ in color_set:
    r = _.rgb.r
    g = _.rgb.g
    b = _.rgb.b
    rgb = (r, g, b)
    color_set_rgb.append(rgb)

# 거북이 선언
timmy = Turtle()
timmy.shape("turtle")

# RGB colormode 설정
colormode(255)


def draw_simple_hirst(spacing, circle_size, color_set):
    timmy.speed("fastest")
    # timmy.right(180)
    # timmy.penup()
    # timmy.forward(10*spacing)
    # timmy.left(90)
    # timmy.pendown()
    timmy.penup()
    timmy.setposition(5*spacing, -5*spacing)
    #  10 by 10 dots
    #  circles {circle_size} in size spacing {spacing}
    for horizontal in range(0, 10):
        timmy.penup()
        timmy.left(90)
        timmy.forward(spacing)
        timmy.left(90)
        timmy.forward(10 * spacing)
        timmy.right(180)
        timmy.pendown()
        for parallel in range(0, 10):
            timmy.dot(circle_size, random.choice(color_set))
            timmy.penup()
            timmy.forward(spacing)
            timmy.pendown()


# set up screen
sc = Screen()

draw_simple_hirst(100, 40, color_set_rgb)

sc.mainloop()