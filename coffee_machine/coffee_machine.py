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

def is_machine_on():
    isOn = True
    for item in coffee_machine:
        if item != 'money' and coffee_machine[item]['amount'] == 0:
            isOn = False
            break
    return isOn

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

def charge_for_drink(drink_price):
    transaction = {
        'cleared': True,
        'change': 0
    }
    try:
        quarters = int(input(f"{strings.ask_for_quarters} "))
        quarters = quarters * coin_values.cents['Quarter']
    except ValueError:
        quarters = 0
    try:
        dimes = int(input(f"{strings.ask_for_dimes} "))
        dimes = dimes * coin_values.cents['Dime']
    except ValueError:
        dimes = 0
    try:
        nickles = int(input(f"{strings.ask_for_nickles} "))
        nickles = nickles * coin_values.cents['Nickel']
    except ValueError:
        nickles = 0
    try:
        pennies = int(input(f"{strings.ask_for_pennies} "))
        pennies = pennies * coin_values.cents['Penny']
    except ValueError:
        pennies = 0
    total_cents = quarters + dimes + nickles + pennies
    if total_cents >= drink_price:
        transaction['change'] = total_cents - drink_price
    else:
        transaction['cleared'] = False
    return transaction

def get_change(transaction_change):
    change = transaction_change
    if change > 0:
        change =  change / 100
        change = "%.2f" % change
    return change

def update_coffee_machine(drink):
    coffee_machine['money']['amount'] = coffee_machine['money']['amount'] + drink['price']
    for ingredient in drink['recipe']:
        coffee_machine[ingredient]['amount'] = coffee_machine[ingredient]['amount'] - drink['recipe'][ingredient]['amount']
    
def run_service():
    drink_order = input(strings.prompt_for_order).lower()
    if drink_order == REPORT:
        print_report(coffee_machine)
    else:
        drink_details = get_drink_details(drink_order)
        if drink_details["recipe"] == NOT_FOUND:
            print(strings.bad_order_message)
        else:
            is_machine_stocked = check_machine_resources(drink_details, coffee_machine)
            if is_machine_stocked['can_make_drink'] == False:
                print(f"{strings.not_ennough_message} {is_machine_stocked['reason']}.")
            else:
                cost = drink_details['price'] / 100
                cost = "%.2f" % cost
                print(f"{strings.that_will_cost} {cost}.")
                print(strings.insert_coins)
                transaction = charge_for_drink(drink_details['price'])
                if transaction['cleared'] == False:
                    print(strings.not_enough_money)
                else:
                    if(transaction['change']) > 0:
                        change = get_change(transaction['change'])
                        print(f"{strings.here_is} ${change} {strings.in_change}")
                    update_coffee_machine(drink_details)
                    print(f"{strings.here_is_your} {drink_order}. {strings.enjoy}")

def init():
    can_serve = True        
    while can_serve == True:
        run_service()
        can_serve = is_machine_on()
        if can_serve == False:
            print(strings.machine_off_message)

init()
