import art
import game_data
import random 
from replit import clear 

want_to_play=input("Do you want to play the higher/lower game? (Type 'y' or 'n') : ").lower()
while want_to_play!='y' and want_to_play!='n':
    want_to_play=input("Please choose from the answers (Type 'y' or 'n') : ").lower()
lost=False
# ask if you want to play the game 
while want_to_play=='y':
  clear()
  print(art.logo)
  lost=False
  score=0

  while lost==False:
    # pick two random results
    option_a=random.randint(0,50)
    option_b=random.randint(0,50)
    while option_b==option_a:
      option_b=random.randint(0,50)

    # show two random results
    print(f"Option A is '{game_data.data[option_a]['name']}' who/which is '{game_data.data[option_a]['description']}' from '{game_data.data[option_a]['country']}' ")
    print("")
    print("")
    print(art.vs)
    print("")
    print("")
    print(f"Option B is '{game_data.data[option_b]['name']}' who/which is '{game_data.data[option_b]['description']}' from '{game_data.data[option_b]['country']}' ")
    print("")
    print("")
    # let the user choose 
    choice=input("What's your chioce? (Type 'a' or 'b': )").lower()
    while choice!='a' and choice!='b':
        input("Please choose from the answers (Type 'a' or 'b') : ").lower()


    if game_data.data[option_a]['follower_count']>game_data.data[option_b]['follower_count']:
      winning_data='a'
    else:
      winning_data='b'
      
    # tell the user about his/her result 
    if choice==winning_data:
      print("You are Right!")
      score+=1
      print(f"Your Current score is : {score}")
    else:
      print("You are wrong")
      lost=True
      want_to_play=input("Do you want to play the higher/lower game? (Type 'y' or 'n') : ").lower()
    
    



  # show if the user is right or wrong 


  


# if right, to next question


# if wrong, to the question 

# ask if you want to play again


