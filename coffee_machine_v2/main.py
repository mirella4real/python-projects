from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
print(my_menu.get_items())
print(my_menu.find_drink('ltte').name)

my_coffee_maker = CoffeeMaker()
print(my_coffee_maker.report())