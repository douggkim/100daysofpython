from data import question_data
from question_model import question
from quiz_brain import QuizBrain

# import question_model

question_bank = []
for data in question_data["results"]:
    question_bank.append(question(data["question"], data["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was : {quiz_brain.score}/{len(question_bank)}")
# print(question_bank[0].text)
