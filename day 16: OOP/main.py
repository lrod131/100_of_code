'''
This is the same coffee machine project but this time using OOP for practicing
'''

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

#creating objects
current_menu = Menu()
#menu_items = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
pay = MoneyMachine()
coffee = CoffeeMaker()

#starting the program
user_input = input(f'What would you like? ({current_menu.get_items()}): ')
while user_input != 'off':
    if user_input == 'report':
        coffee.report()
        pay.report()

    if user_input in current_menu.get_items():
        selected_coffee = current_menu.find_drink(user_input)
        if coffee.is_resource_sufficient(selected_coffee):
            if pay.make_payment(selected_coffee.cost):
                coffee.make_coffee(selected_coffee)

    user_input = input(f'What would you like? ({current_menu.get_items()}): ')
