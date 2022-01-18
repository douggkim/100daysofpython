# ---------------------------------------------------
# Control Flow with if/ else and Conditional Operators
water_level=50
if water_level>80:
  print("tub is not full")
else:
  print("water level is full")

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, You cannot ride the rollercoaster")


# ---------------------------------------------------
# Nested if statements and elif statements 


print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster")
  age=int(input("What is your age?"))
  if age< 12:
    print("Please pay $5")
  elif age<=18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("Sorry, You cannot ride the rollercoaster")

# ---------------------------------------------------
# Multiple if Statements in Succession

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster")
  age=int(input("What is your age?"))
  if age< 12:
    bill=5
    print("Child Tickets are $5")
  elif age<=18:
    bill=7
    print("Youth tickets are $7")
  else:
    bill=12
    print("Adult tickets are $12")
  
  wants_photo=input("Do you want a photo taken? Y or N. ")
  if wants_photo=="Y":
    bill+=3
 
  print(f"you have to pay {bill}")
else:
  print("Sorry, You cannot ride the rollercoaster")


# ---------------------------------------------------
# Logical Operators & Others

#   elif age>=45 and age<=55:
#     print("Don't Worry the bill is on us")