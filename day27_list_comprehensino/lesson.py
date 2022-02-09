numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(n)

new_list = [n for n in numbers]
# add 1 for every item in the list numbers
new_list = [n + 1 for n in numbers]

# [2,4,6,8]
range_list = [2 * n for n in range(1, 5)]

# 조건부로도 활용 가능
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
upper_names = [name.upper() for name in names if len(name) >= 5]

# dict 사용 방법
# new_dict = {new_key: new_value for item in list }
# new_dict = {new_key: new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value)in dict.items() if condition}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_scores = {student: random.randint(0, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 10}
print(passed_students)

import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(index)  # 1,2,3
    print(row)  # student, score 를 따로따로 print
    print(row.student)  # student 각자의 이름을 뽑음

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.student())
