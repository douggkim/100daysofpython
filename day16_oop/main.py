# from turtle import Turtle 도 가능
import turtle

# turtle 모듈에서 Turtle  클래스를 조회
timmy = turtle.Turtle()
# <turtle.Turtle at 0x1016fc8540>
print(timmy)
# set the shape of the icon
timmy.shape("turtle")
# set the color of the icon
timmy.color("coral")
# move the turtle by 100
timmy.forward(100)

# turtle 을 띄울 배경을 로딩함
my_screen = turtle.Screen()
print(my_screen.canvheight)
# 클릭 시 종료
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Bulbasaur"])

# "pokemon Name" 칼럼의 정렬 변경
table.align["Pokemon Name"] = "l"
# table의 정렬을 확인
print(table.align)

table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

