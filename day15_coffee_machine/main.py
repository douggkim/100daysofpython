from data import MENU, resources

# TODO starting_ingredient
remaining_water = resources["water"]
remaining_milk = resources["milk"]
remaining_coffee = resources["coffee"]
remaining_money = 0


# TODO make coffee function
def make_coffee(choice, water, milk, coffee, money):
    water -= MENU[choice]["ingredients"]["water"]
    coffee -= MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        milk -= MENU[choice]["ingredients"]["milk"]
    money += MENU[choice]["cost"]

    return [water, milk, coffee, money]


# TODO check resources
def check_resources(choice):
    if choice != "espresso":
        # if remaining_milk is not None:
        if remaining_milk < MENU[choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return False
    if remaining_water < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    if remaining_coffee < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        # water-=MENU[choice]["ingredients"]["water"]
        # milk -= MENU[choice]["ingredients"]["milk"]
        # coffee -= MENU[choice]["ingredients"]["coffee"]
        #
        return True


# TODO process coins
def receive_payment(coffee):
    price = MENU[coffee]["cost"]
    quarter = float(input("How many quarters? : "))
    dimes = float(input("How many dimes? : "))
    nickles = float(input("How many nickles? : "))
    pennies = float(input("How many pennies? : "))
    payment_total = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if payment_total > price:
        change_total = payment_total - price
        print(f"Here is {change_total} dollars in change.")
        return True
    elif payment_total == price:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


choice = ""

while choice != "off":
    # TODO Turn off the Coffee Machine by entering “off” to the prompt
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    # TODO print report
    if choice == "report":
        print(f"Water : {remaining_water} ml")
        print(f"Milk : {remaining_milk} ml")
        print(f"Coffee : {remaining_coffee} ml")
        print(f"Money : $ {remaining_money}")
    elif choice == 'espresso' or choice == "latte" or choice == "cappuccino":
        # print("choice done. ")
        if check_resources(choice):
            # print("resources done. ")
            if receive_payment(choice):
                # print("payments done")
                coffee_result = make_coffee(choice, remaining_water, remaining_milk, remaining_coffee, remaining_money)
                remaining_water = coffee_result[0]
                remaining_milk = coffee_result[1]
                remaining_coffee = coffee_result[2]
                remaining_money = coffee_result[3]
                print(f"Here is your {choice}. Enjoy!☕")
    elif choice == "off":
        continue
    else:
        print("Please choose a valid option. (espresso/latte/cappuccino) ")

# TODO check resources sufficient?


# TODO check transaction successful?


# coffee emoji ☕
