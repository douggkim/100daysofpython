from tkinter import *
import pandas as pd
import random

# global variable
BACKGROUND_COLOR = "#B1DDC6"

# process dict data
vocab_raw = pd.read_csv("./data/french_words.csv")
vocab_dict = vocab_raw.to_dict(orient="records")


def reset_vocab():
    global flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(vocab_dict)
    random_word_en = random_word["English"]
    random_word_fr = random_word["French"]
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(word_text, fill="black", text=random_word_fr)
    canvas.itemconfig(lang_text, fill="black", text="French")
    flip_timer = window.after(3000, turn_card)

def turn_card():
    french_word = canvas.itemcget(word_text, "text")
    print(french_word)
    for word in vocab_dict:
        print(word)
        if word["French"] == french_word:
            english_word = word["English"]
            print(english_word)
            break
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(lang_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=english_word)


# create window
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create card_image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
# create text
lang_text = canvas.create_text(400, 150, text="French", font=("arial", 40, "italic"), tag="lang")
word_text = canvas.create_text(400, 263, text="donne", font=("arial", 60, "bold"), tag="word")

# timer global
flip_timer = window.after(3000, turn_card)

back_img = PhotoImage(file="./images/card_back.png")

# import & create buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=reset_vocab)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=reset_vocab)
wrong_button.grid(row=1, column=0)

window.mainloop()
