import turtle
import pandas as pd

# define screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# define turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")

turtle.shape(image)

# load the data
map_data = pd.read_csv("50_states.csv")


# 클릭해서 좌표를 얻음
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

guessed_states = []

while len(guessed_states) < 50:
    # prompt for inputting answers
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?")
    for state in map_data["state"]:
        if answer.title() == state:
            # 아래에 int() 로 감싸줘서 숫자로 만들어줄 수 도 있음 / dataframe.item() 으로도 가능
            x_cor = map_data[map_data["state"] == answer.title()]["x"].values[0]
            y_cor = map_data[map_data["state"] == answer.title()]["y"].values[0]
            coordinate = (x_cor, y_cor)
            writer.setpos(x_cor, y_cor)
            writer.write(answer.title(), align="center", font=("Verdana", 5, "normal"))
            guessed_states.append(answer.title)
        elif answer.lower() == "end":
            # or break
            guessed_states = range(51)

# get the index of the data which the user did not get right
states_to_learn_idx = ~map_data.state.isin(guessed_states)
states_to_learn = map_data[states_to_learn_idx]
# record the data as a csv file
states_to_learn.to_csv("states_to_learn.csv")
# keeping the screen open even though the code finished running
turtle.mainloop()
