from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


# 변수로 해당 객체만 올 수 있다고 정의해놓을 필요가 있음
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create card - canvas 에도 padding 넣을 수 있다.
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # create_text 에 대해서 text_width 를 지정해서 특정 공간 안에 들어가도록 할 수 있음
        self.question_text = self.canvas.create_text(150, 125, text="questions", font=("arial", 20, "italic"),
                                                     fill=THEME_COLOR, width=280)

        # create buttons
        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        # create scores
        self.score = Label(text=f"Score : 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)
        self.refresh_score()

    def refresh_score(self):
        self.score.config(text=f"Score : {self.quiz.score}")
