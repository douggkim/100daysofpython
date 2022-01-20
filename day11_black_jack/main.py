############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace. Jack, queen, king = 10
#  ace = 1 if >20 
# each card has equal chance of occurring


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
from replit import clear 
import random 


def play_game():
  clear() 
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  # deal both user and computer a starting hand of two 
  user_cards=[]
  computer_cards=[]

  def random_card(list):
    for i in range(0,2):
      list.append(int(cards[random.randint(0,12)]))

  random_card(user_cards)
  random_card(computer_cards)


  # detect when computer or user has a blackjack (ace+10 value card)

  def check_blackjack(deck):
    for card_one in deck:
      if card_one==11:
        for card_two in deck: 
          if card_two==10:
            return True
      else:
        return False

  # if computer gets blackjack then the user loses (even if the user has blackjack)
  if check_blackjack(computer_cards):
    #user loses
    print("You lose")

  # if the user gets the black jack, user wins (unless the computer also has a blackjack)
  if check_blackjack(user_cards):
    print("You Win!")
  # calculate the user's and computer's score based on their card values 
  # if an ace is drawn. 11  / if >21 1 
  def calculate_cards(cards):
    """Add all the cards which are chosen"""
    if sum(cards)>=21:
      for card in cards:
        if card==11:
          card=1
          return(sum(cards)-10)
    return sum(cards)

  #  reveal computer's first card to the user 
  print(f"Computer's first card is {computer_cards[0]}")
  print("==========================")
  # game ends immediately when user score goes over 21 or if the user or computer gets a blackjack
  user_sum_one=calculate_cards(user_cards)
  computer_sum_one=calculate_cards(computer_cards)
  
  print(f"Your card is {user_cards}")
  print(f"Your sum of cards is {user_sum_one}")
  print("==========================")

  # ask the user if he/she wants to get another card
  if input("Do you want to draw another card? Type 'y' or 'n' : ").lower()=='y':
    user_cards.append(int(cards[random.randint(0,12)]))
  print("==========================")

  print("You have drawn your cards.")
  print("==========================")

  # once the user chooses, let the computer play. the computer should keep drawing cards unless their score goes over 16 
  if computer_sum_one<=16:
    computer_cards.append(int(cards[random.randint(0,12)]))
    print("Computer has drawn its card.")
    print("==========================")
  else:
    print("Computer chose not to draw.")

  # compare score. see if win, loss, or draw
  user_sum_final=calculate_cards(user_cards)
  computer_sum_final=calculate_cards(computer_cards)
  # print out the player's and computer's final hand and their scores at the end of the game 
  print(f"Computer's cards: {computer_cards}")
  print(f"Computer's final score: {computer_sum_final}")
  print("")
  print(f"Your cards: {user_cards}")
  print(f"Your final score: {user_sum_final}")
  print("==========================")
  def check_over_twenty_one(deck):
    """Check if any of the card is over the number 21"""
    if deck>21:
      return True
  
  if check_over_twenty_one(computer_sum_final) and check_over_twenty_one(user_sum_final):
    print("It's a tie.")
  elif  check_over_twenty_one(user_sum_final):
    print("You lose.")
  elif check_over_twenty_one(computer_sum_final):
    print("You Win.")
  else:
    if user_sum_final>computer_sum_final:
      print("You won!")
    elif user_sum_final<computer_sum_final:
      print("You lose.")
    else:
      print("It's a tie.")
  # after the game ends ask the user if they'd like to play again. if yes clear console 
  if input("Do you want to play again? Type 'y' or 'n' : ").lower()=="y":
    play_game()


play_game()


# while restart.lower()=='y':
  
  
