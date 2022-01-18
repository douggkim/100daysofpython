from art import logo
# from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)

bidder_dict={}
#  ask if there are other users who want to bid
while(input("Is there any other bidder?").lower()=="yes"):


  bidder_temp_list=[]
  # ask for name input 
  name=input("What is his/her name?")
  # bidder_temp_list.append(name)
  # ask for bid price
  bid_price=input("What is the bidding price?")
  # bidder_temp_list.append(bid_price)
  # add name and bid into a dictionary as the key and value 
  bidder_dict[name]=bid_price
  
  # clear the screen 
  # clear()

highest_bid=0
for bidder_name in bidder_dict:
  if(int(bidder_dict[bidder_name])>highest_bid):
    highest_bid=int(bidder_dict[bidder_name])

print(highest_bid)



# NO - find the highest bid in the dictionary and declare them as the winner