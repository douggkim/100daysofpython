from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(menu.find_drink("espresso").name)

while machine_on:
    choice = input(f"What would you like? {menu.get_items()}:").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
        continue

    elif hasattr(menu.find_drink(choice), "name"):
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
            money_machine.make_payment(menu.find_drink(choice).cost)
            coffee_maker.make_coffee(menu.find_drink(choice))
        else:
            print("Sorry there is not enough ingredient")
    else:
        print(f"Please choose a valid option. {menu.get_items()}:")
