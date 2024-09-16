import strings
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_register = MoneyMachine()
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
REPORT = 'report'
OFF = 'off'

def print_report(coffee_maker):
    print(coffee_maker.report()) 

def run_service():
    """Virtual waiter. Prompts for drink order and functionality for verifying, serving and charging for drink."""
    can_continue_service = True
    drink_order = input(f"{strings.prompt_for_order} {my_menu.get_items()}: ").lower()
    if drink_order == REPORT:
        print_report(my_coffee_maker)
    elif drink_order == OFF:
        can_continue_service = False
    else:
        ordered_menu_item = my_menu.find_drink(drink_order)
        if ordered_menu_item.get_name() == "":
            print(strings.bad_order_message)
        else:
            can_serve = my_coffee_maker.is_resource_sufficient(ordered_menu_item)
            if can_serve['can_serve'] == False:
                print(f"{strings.not_ennough_message} {can_serve['reason']}.")
            else:
                cost = ordered_menu_item.get_cost()
                cost = "%.2f" % cost
                print(f"{strings.that_will_cost} {cost}.")
                print(strings.insert_coins)
                payment_cleared = my_register.make_payment(ordered_menu_item.get_cost())
                if payment_cleared == False:
                    print(strings.not_enough_money)
                else:
                    if my_coffee_maker.make_coffee(ordered_menu_item) == True:
                        print(f"{strings.here_is_your} {drink_order}. {strings.enjoy}")
    return can_continue_service

def init():
    """Initializes coffee service and repeats until coffee machine can no longer serve or is turned off."""
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