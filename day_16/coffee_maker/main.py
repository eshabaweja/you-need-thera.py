from random import random

from requests import options
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

money_machine = MoneyMachine()
menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print("Here's the report!")
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink)) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                