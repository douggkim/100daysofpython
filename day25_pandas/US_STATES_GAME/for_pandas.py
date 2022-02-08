import pandas as pd

map_data = pd.read_csv("50_states.csv")

while True:
    answer = input("input the state : ")
    for state in map_data["state"]:
        if answer.title() == state:
            x_cor = map_data[map_data["state"] == answer]["x"].values[0]
            y_cor = map_data[map_data["state"] == answer]["y"].values[0]
            coordinate = (x_cor, y_cor)
