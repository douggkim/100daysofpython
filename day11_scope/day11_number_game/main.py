import random
from art import logo
from replit import clear
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def number_game():
  EASY_ATTEMPT=10
  HARD_ATTEMPT=5
  clear()
  print(logo)
  print("Welcome to the Number guessing game!")

  print("I'm thinking of a number between 1 and 100")
  random_num=random.randint(1,101)

  if input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()=='easy':
    print(f"You have {EASY_ATTEMPT} attempts remaining to guess the number.")

    while EASY_ATTEMPT>0:
      print(f"You have {EASY_ATTEMPT} attempts left.")
      guess=int(input("Make a guess : "))
      if random_num > guess:
        print("Too low.")
        EASY_ATTEMPT-=1
      elif random_num < guess:
        print("Too high.")
        EASY_ATTEMPT-=1
      else: 
        print("You got it right!")
        if input("Do you want to play again?").lower()=='y':
          number_game()

  elif input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()=='hard':
    print(f"You have {HARD_ATTEMPT} attempts remaining to guess the number.")

    while HARD_ATTEMPT>0:
      print(f"You have {HARD_ATTEMPT} attempts left.")
      if random_num > int(input("Make a guess : ")):
        print("Too low.")
        HARD_ATTEMPT-=1
      elif random_num < int(input("Make a guess : ")):
        print("Too high.")
        HARD_ATTEMPT-=1
      else: 
        print("You got it right!")
        if input("Do you want to play again?").lower()=='y':
          number_game()
    print("You have run out of attemps!")

  else:
    number_game()
  if input("Do you want to play again?").lower()=='y':
    number_game()

number_game()

      



