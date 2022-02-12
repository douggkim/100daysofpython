import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# window 설정
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas 및 이미지 설정
canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# columnspan : 해당 컬럼에서 시작해서 해당 요소가 몇 개까지 걸쳐있는지 표현

# TODO 1 : label
website_label = tkinter.Label(text="Website:", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0)

user_label = tkinter.Label(text="Email/Username:", font=("Arial", 12, "bold"))
user_label.grid(row=2, column=0)

pw_label = tkinter.Label(text="Password:", font=("Arial", 12, "bold"))
pw_label.grid(row=3, column=0)

# TODO 2 : textbox

website_text = tkinter.Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2)

user_text = tkinter.Entry(width=35)
user_text.grid(row=2, column=1, columnspan=2)

pw_text = tkinter.Entry(width=21)
pw_text.grid(row=3, column=1, columnspan=1)

# TODO 3 : Buttons
pw_button = tkinter.Button(text="Generate Password", width=15)
pw_button.grid(row=3, column=2, columnspan=1)

add_button = tkinter.Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
