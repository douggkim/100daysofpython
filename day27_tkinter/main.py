from tkinter import *

# TODO 1: window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# TODO 2 : input - miles number
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)
miles_input.focus()

# TODO 2 : label - Miles
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# TODO 3 : label - is equal to
equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

# TODO 4 : label - km number
km_num_label = Label(text="0")
km_num_label.grid(row=1, column=1)

# TODO 5 : label - km
km_label = Label(text="km")
km_label.grid(row=1, column=2)


# TODO 6 : button - calculate
def calculate_button():
    km_num_label["text"] = float(miles_input.get()) * 1.60934


button = Button(text="calulate", command=calculate_button)
button.grid(row=2, column=1)

window.mainloop()
