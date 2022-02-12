from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # IF it's the 1st/ 3rd / 5th/ 7th rep:
    if reps % 2 != 0:
        reps += 1
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
        count_down(work_sec)

    # If it's the 8th rep:
    elif reps == 8:
        reps = 1
        timer_label["text"] = "Break"
        timer_label["fg"] = RED
        count_down(long_break_sec)

    # if it's 2nd/ 4th / 6th rep:
    else:
        reps += 1
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # canvas 안의 요소는 canvas.itemconfig()로 접근해야 함
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # after : 일정시간이 지난 후 함수를 실행시키는 함수
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
            checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# TODO 1 : Label
# label에는 foreground로 색 설정
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

#  TODO 2 : image
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
# canvas 에는 Photoimage 라고 변환해서 넣어야함
tomato_img = PhotoImage(file="tomato.png")
# 아래의 x,y좌표는 중간 좌표를 넣어야 함
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# TODO 3: start-button
def start_button_clicked():
    start_timer()


start_button = Button(text="Start", command=start_button_clicked, highlightthickness=0)
start_button.grid(row=2, column=0)

# TODO 4: Reset-button

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

# TODO 5: Checkmark ✔
checkmark = Label(text="", height=5, width=5, font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)

window.mainloop()
