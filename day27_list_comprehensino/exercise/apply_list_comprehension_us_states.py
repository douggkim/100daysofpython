while len(guessed_states) < 50:
    # prompt for inputting answers
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?")

    guess_states = [state for state in map_data["state"] if answer.title() == state]
    x_cor = map_data[map_data["state"] == answer.title()]["x"].values[0]
    y_cor = map_data[map_data["state"] == answer.title()]["y"].values[0]
    writer.setpos(x_cor, y_cor)
    writer.write(answer.title(), align="center", font=("Verdana", 5, "normal"))
    if answer.lower() == "end":
        # or break
        guessed_states = range(51)