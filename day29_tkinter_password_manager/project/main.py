import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    # password_list 안의 요소들을 함께 합침
    password = "".join(password_list)
    pyperclip.copy(password)
    pw_text.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_text.get()) == 0 or len(user_text.get()) == 0 or len(pw_text.get()) == 0:
        messagebox.showinfo(title="Warning", message="Don't leave any information empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text.get(),
                                       message=f"These are the details entered : \n Email: {user_text.get()} \n Password: {pw_text.get()}\n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_txt:
                print(pw_text.get())
                data_txt.write(website_text.get() + "| " + user_text.get() + " | " + pw_text.get() + "\n")
                website_text.delete(0, "end")
                user_text.delete(0, "end")


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
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)

pw_label = tkinter.Label(text="Password:")
pw_label.grid(row=3, column=0)

# TODO 2 : textbox

website_text = tkinter.Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

user_text = tkinter.Entry(width=35)
user_text.insert(0, "slakingex@naverr.com")
user_text.grid(row=2, column=1, columnspan=2)

pw_text = tkinter.Entry(width=21)
pw_text.grid(row=3, column=1)

# TODO 3 : Buttons
pw_button = tkinter.Button(text="Generate Password", command=generate_password)
pw_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
