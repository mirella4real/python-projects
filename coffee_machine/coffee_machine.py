import coffee_flavors
import machine_capacity
import coin_values 
import strings

COFFEE = 'coffee'
WATER = 'water'
MILK = 'milk'
MONEY = 'money'
REPORT = 'report'
NOT_FOUND = 'not found'
coffee_machine = machine_capacity.initial_capacity

def print_report(machine):
    print(f"{strings.water}:  {machine[WATER]['amount']}{machine[WATER]['unit']}")
    print(f"{strings.milk}:   {machine[MILK]['amount']}{machine[MILK]['unit']}")
    print(f"{strings.coffee}: {machine[COFFEE]['amount']}{machine[COFFEE]['unit']}")
    print(f"{strings.money}:  {machine[MONEY]['amount']}{machine[MONEY]['unit']}")

def get_drink_details(drink_order):
    """Retrieves and returns drink recipe and cost or 'not found' flag"""
    try:
        drink_details = coffee_flavors.data[drink_order]
    except KeyError:
        drink_details = {
            'recipe': NOT_FOUND,
            'order': drink_order
        }
    return drink_details

def check_machine_resources(drink_details, machine):
    machine_status = {
        'can_make_drink': True
    }
    for ingredient in drink_details['recipe']:
        if machine[ingredient]['amount'] < drink_details["recipe"][ingredient]['amount']:
            machine_status['can_make_drink'] = False
            machine_status['reason'] = ingredient
            break
    return machine_status

def run_service():
    can_serve = True
    drink_order = input(strings.prompt_for_order).lower()
    if drink_order == REPORT:
        print_report(coffee_machine)
        can_serve = True
    else:
        drink_details = get_drink_details(drink_order)
        if drink_details["recipe"] == NOT_FOUND:
            print(strings.bad_order_message)
            can_serve = True
        else:
            is_machine_stocked = check_machine_resources(drink_details, coffee_machine)
            if is_machine_stocked['can_make_drink'] == False:
                print(f"{strings.not_ennough_message} {is_machine_stocked['reason']}.")
                can_serve = True
            else:
                cost = drink_details['price'] / 100
                cost = "%.2f" % cost
                print(f"{strings.that_will_cost} {cost}.")
                print(strings.insert_coins)
                quarters = int(input(f"{strings.ask_for_quarters} "))
                dimes = int(input(f"{strings.ask_for_dimes} "))
                nickles = int(input(f"{strings.ask_for_nickles} "))
                pennies = int(input(f"{strings.ask_for_pennies} "))
                can_serve = False
            can_serve = False
    return can_serve

def init():
    can_serve = True        
    while can_serve == True:
        can_serve = run_service()

init()
