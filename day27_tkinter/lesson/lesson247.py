from tkinter import *

window = Tk()
window.title("My First GUI program")
# 초기 window size 를 결정
window.minsize(width=500, height=300)

# Label은 별도 정의를 해주고 어떤 식으로 표현해줄지 정의해줘야 함
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# pack() : screen에 넣고 기본적으로 중간에 위치시킴 (label 외 다른 경우에도 적용 가능)
# expand 옵션 : 모든 공간을 활용
my_label.pack()

# 하기의 모든 방법으로 text 를 바꿀 수 있음
my_label["text"] = "New Text"
my_label.config(text="New Text")


# button 눌릴 때 적용시킬 함수
def button_clicked():
    # input 값을 string으로 받음
    my_label["text"] = input.get()


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

# text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with
# END : index, 어디인지 가리켜줌? 항상 이렇게 씀.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    #     gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used():
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    #     Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    #     Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Grape"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# mainloop() : 계속 사용자의 action 을 기다리도록 함
window.mainloop()
