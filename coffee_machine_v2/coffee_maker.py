from prettytable import PrettyTable
class CoffeeMaker:

    def __init__(self):
        self.type_of = "CoffeeMaker"
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def get_type_of(self):
        return self.type_of
    
    def get_resource_amount(self, resource):
        return self.resources[resource]   
    
    def report(self):
        table = PrettyTable()
        table.add_column("Resource", ['water', 'milk', 'coffee'])
        table.add_column("Amount", [self.get_resource_amount('water'), self.get_resource_amount('milk'), self.get_resource_amount('coffee')])
        table.align = "l"
        return table
    
    def is_machine_on(self):
        """Checks if any resoruces are at 0 and returns Boolean accordingly."""
        isOn = True
        for item in self.resources:
            if self.resources[item] == 0:
                isOn = False
                break
        return isOn
    
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                can_make = False
        return can_make
    
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        return True