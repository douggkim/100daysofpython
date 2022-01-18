# ---------------------------------------------------
# Using the loop with Python lights 
# for item in list_of_items: 
#   #Do something
  
fruits = ["apple","pear","peaches"]
for fruit in fruits: 
  print(fruit)
  print(fruit + " Pie")

# ---------------------------------------------------
# For loops and range() function
a=1
b=10
for number in range(a,b):
  print(number)

#1~ 9까지 숫자 인쇄 
for number in range(1,10):
  print(number)
  
total=0

for number in range(1,101):
  total+=number
print(total)