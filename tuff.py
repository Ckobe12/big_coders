"""Kobe's Code (Methods)"""

class Restaurant:
    def __init__(self,name):
        self.name = name 
        self.waiter = Waiter()

    def welcoming_customer(self):
        print(f"Welcome to {self.name}!")
        self.waiter.greet_customer()

class Waiter: 

    def greet_customer(self): 
        party_size=self.ask_size()
        print(f"Awesome! Since your party size is {party_size}. Let me show you to your table!")  
def ask_size(self):
    """Will be a method that allows the user to enter a party size. """



'''Joaddan's Code'''
class MenuItem:
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords
        

class Menu:
    def __init__(self):
        self.foods = []

    def add_food(self, food):
        self.foods.append(food)

    def display_menu(self):
        print("Menu:")
        for food in self.foods:
            print(f"{food.name}")

    def find_food(self, keyword):
        matches = []
        for food in self.foods:
            if keyword.lower() in food.keywords:
                matches.append(food)
        return matches
    
'''John's Code'''
def take_orders(customer_info, menu):
    '''Takes orders from customers based on a given menu.
    
    Args:
    customer_info (list of tuples): contains customer info, which consist of the
                                    customer's name and their party size.
    menu (Menu): Instance of the Menu class showing the available menu options
    
    Returns:
    dict: A dictionary that has the order for each person with the keys being their names and values as the list of ordered food.
    
    
    '''
    orders = {}
    for person, party_size in customer_info:
        print(f'Ordering for person {person}:')
        orders[person] = []
        for i in range(party_size):
            order = input('What would you like to eat today?')
            matches = menu.find_food(order)
            if matches:
                print(f'Menu items matching "{order}":')
                for match in matches:
                    print(match.name)
                waiter = input("Please choose an item you would like to eat:")
                orders[person].append(waiter)
            else:
                print("Sorry, we don't have that item on the menu, please choose something else.")
                orders[person].append(None)
    return orders

def billcalc(orders, menu):
    '''Calculating the total bill for each person based on their orders.
    Args:
        orders(dict): A dict havinng all the orders for each person.
        menu(Menu): An instance of the Menu class showing the options.
        
    Returns:
        dict: A dictionary having the total bill for each person.
    '''
    bill = {}
    for person, order_list in orders.items():
        total_price = 0
        for item in order_list:
            for food in menu.foods:
                if item == food.name:
                    total_price += food.price
                    break
        bill[person] = total_price
    return bill
        
    




'''Neil's Code'''

class Waiter:
    
    """Initializes a class called waiter who assigns guests to the corresponding table"""

    def __init__(self, restaurant_tables):
        self.restaurant_tables = restaurant_tables
    
    """Initializes restaurant tables with each table having a guest capacity"""

    def assign_guests (self, num_guests):
        
        """Initializes the number of guests to correspond to a table
        
        Args:
            num_guests(int): number of guests waiting to be seated 
            """    
        
        assigned = False
        for table, capacity in self.restaurant_tables.items():
            if num_guests <= capacity:
                self.restaurant_tables[table] -= num_guests
                print(f"Assigned {num_guests} guests to table {table}.")
                assigned = True
                break
        if not assigned:
            print("No available table to accommodate the guests.")

restaurant_tables = {
    1: 2,
    2: 4,
    3: 6,
    4: 8,
    5: 10
}

waiter = Waiter(restaurant_tables)

num_guests = int(input("Enter the number of guests: "))

waiter.assign_guests(num_guests)
print("Updated table assignments:", restaurant_tables)

