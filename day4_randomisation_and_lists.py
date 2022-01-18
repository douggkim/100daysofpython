# ---------------------------------------------------
# Random Module

import random 

#100~200 사이에서 랜덤한 integer 를 고름
random_int=random.randint(100,200) 

#부동소수점 숫자를 랜덤하게 뽑아내기 위해
#0에서 1 미만의 숫자를 뽑아냄
random_float=random.random() 

# ---------------------------------------------------
# Understanding the Offset and Appending Items to Lists 

fruits=["cherry","apple","pear"]

states_of_america = ["Delaware","Pennsylvania","New Jersey"]
print(states_of_america[0])

#모든 요소 보기 
print(states_of_america)

#음수의 index - 뒤에서 세기 시작함 - > New Jersey 뽑음 
print(states_of_america[-1])

#리스트 요소 변경 가능
states_of_america[1]="Pencilvania"

#리스트 끝에 단어 추가
states_of_america.append("Angelaland")
print(states_of_america)

#extend -> 여러개를 추가
states_of_america.extend(["A","B","C"])


# ---------------------------------------------------
# Index Errors and Working with Nested Lists
#index out of range 발생 -> 길이는 index 초과
print(len(states_of_america))

#nested lists
dirty_dozen=[["strawberries","Apples","Grapes","Peaches"],["Nectarines","Spinach"]]

#nested lists2 
fruits=["strawberries","Apples","Grapes","Peaches"]
vegies=["Nectarines","Spinach"]

dirty_dozen2=[fruits,vegies]