from art import logo


def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2


operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
  }


def calculator():
  # print starting logo 
  print(logo)
  # input #1
  num1=float(input("What is the first number?"))

  # variable for continuing
  should_continue=True

  # loop if the user answers 'y' 
  while should_continue:
    for key in operations:
      print(key,end=" ")
    # pick a function from operations 
    operation_symbol=input("Pick an operation from the line above: ")
    
    calculation_function=operations[operation_symbol]
    num2=float(input("What is your next number?"))
    answer=calculation_function(num1,num2)
    # print the results 
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    # ask the user if he/she wants to continue
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation:").lower()=='y':
      should_continue=True
      num1=answer
    else:
      # start over - call recursion
      should_continue=False
      calculator()


  
calculator()
