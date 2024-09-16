class Menu:

    def __init__(self):
        type_of = "Menu"
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]

    def get_type_of(self):
        return self.type_of
    
    def get_items(self):
        """Returns the names of all available items in the menu"""
        options = ""
        for item in self.menu:
            options += item.name
            if self.menu.index(item) < len(self.menu) -1:
                options += "/"
        return options
    
    def find_drink(self, order_name):
        """Returns a MenuItem object with drink ingredients. If drink is not found, the object's name property will be empty"""
        menu_item = MenuItem(name="", water=0, milk=0, coffee=0, cost=2.0)
        for item in self.menu:
             if item.name == order_name:
                 menu_item = item
        return menu_item
                    



class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.type_of = "MenuItem"
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    def get_type_of(self):
        return self.type_of
    
    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost
    
    def get_ingredients(self):
        return self.ingredients