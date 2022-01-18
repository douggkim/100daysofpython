# ---------------------------------------------------
# ////printing numbers ////
#Integer _468 출력
print(123+345) 

# 쉼표와 같이 숫자를 보기 편하게 하려면? 
print(123_456_789) #123456789를 출력

#float 
3.141592

#Boolean - true 나 false 일 때만

# ---------------------------------------------------
# ////Type Error, Type Checking and Type Conversion////
num_char =len(input("put in a word"))
#print("your name has "+num_char+" characters.") -> 에러 발생

#integer 일듯 
print(type(num_char))
# num_char를 str으로 변환 
new_num_char=str(num_char) 

a=123
#int 가 뽑힘 
print(type(a))
#string으로 변환 
print(type(str(a)))
#float 로 변환 
a=float(123)

#아래의 답은 170.5 
print(70+float("100.5"))

# ---------------------------------------------------
# ////Number Manipulation and F Strings in Python////
result=4/2
result/=2

#f-String 
score=0
height=1.8
isWinning=True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")