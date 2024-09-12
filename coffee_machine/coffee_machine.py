import coffee_flavors
import machine_capacity
import coin_values 
import strings

COFFEE = 'coffee'
WATER = 'water'
MILK = 'milk'
MONEY = 'money'
REPORT = 'report'
coffee_machine = machine_capacity.initial_capacity

def print_report(machine):
    print(f"{strings.water}:  {machine[WATER]['amount']}{machine[WATER]['unit']}")
    print(f"{strings.milk}:   {machine[MILK]['amount']}{machine[MILK]['unit']}")
    print(f"{strings.coffee}: {machine[COFFEE]['amount']}{machine[COFFEE]['unit']}")
    print(f"{strings.money}:  {machine[MONEY]['amount']}{machine[MONEY]['unit']}")

def run_service():
    order = input(strings.prompt_for_order).lower()
    if order == REPORT:
        print_report(coffee_machine)
    return False

def init():
    can_serve = True        
    while can_serve == True:
        can_serve = run_service()

init()
