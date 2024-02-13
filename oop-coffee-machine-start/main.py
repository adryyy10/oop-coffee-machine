from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Disconnect machine
    if choice == "off":
        break

    # Print current resources
    if choice == "report":
        coffee_maker.report()
        continue

    # Get coffee type
    coffee_choice = menu.find_drink(order_name=choice)
    if not coffee_choice:
        continue

    # Check resources
    enough_resources = coffee_maker.is_resource_sufficient(drink=coffee_choice)
    if not enough_resources:
        continue

    # Insert money and pay
    enough_payment = money_machine.make_payment(cost=coffee_choice.cost)
    if not enough_payment:
        continue

    # Make coffee
    coffee_maker.make_coffee(order=coffee_choice)



