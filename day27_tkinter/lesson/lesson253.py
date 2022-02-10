# place(x=40,y=100)
# grid(row=0,column=1)

from tkinter import *

window = Tk()
window.title("My First GUI program")
# 초기 window size 를 결정
window.minsize(width=500, height=300)
# 테두리에 들어갈 크기를 조절 / 각 요소 별로도 쓸 수 있음
window.config(padx=100, pady=200)

# Label은 별도 정의를 해주고 어떤 식으로 표현해줄지 정의해줘야 함
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# pack() : screen에 넣고 기본적으로 중간에 위치시킴 (label 외 다른 경우에도 적용 가능)
# expand 옵션 : 모든 공간을 활용
my_label.grid(row=0, column=0)

# 하기의 모든 방법으로 text 를 바꿀 수 있음
my_label["text"] = "New Text"
my_label.config(text="New Text")


# button 눌릴 때 적용시킬 함수
def button_clicked():
    # input 값을 string으로 받음
    my_label["text"] = input.get()


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Entry
input = Entry(width=10)
input.grid(row=2 , column=3)

# button2
button2 = Button(text="Button2")
button2.grid(row=0, column=2)

window.mainloop()