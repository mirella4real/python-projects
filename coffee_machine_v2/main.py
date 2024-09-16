import strings
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_register = MoneyMachine()
my_menu = Menu()
my_coffee_maker = CoffeeMaker()


def print_report(coffee_maker):
    print(coffee_maker.report()) 

def run_service():
    can_continue_service = False
    drink_order = input(f"{strings.prompt_for_order} {my_menu.get_items()}: ").lower()
    return can_continue_service

def init():
    can_serve = my_coffee_maker.is_machine_on()
    while can_serve == True:
        can_serve = run_service()
        if can_serve == False:
            print(strings.machine_off_message)
        else:
            can_serve = my_coffee_maker.is_machine_on()
            if can_serve == False:
                print(strings.machine_empty_message)

init()