import argparse
import csv
""" Kobe's Code"""
class Restaurant: 
    """_summary_
    """
    def __init__(self,name, waiter):
        """_summary_

        Args:
            name (str): _description_
            waiter (str): _description_
        """
        self.name = name
        self.waiter = waiter
        
    def welcome_guest(self):
        """_summary_
        """
        print(f"Welcome to {self.name}!")
    
    def ask_party_size(self):
        """_summary_
        """
        party_size = int(input("How many guests are in your party today?"))
        self.waiter.party_size = party_size

    def ask_waiter_to_serve(self):
        """_summary_
        """
        self.waiter.welcome_guest()
        self.waiter.assign_guests()# 
        self.waiter.take_orders#waiter takes orders
        self.waiter.calculates_orders # waiter calculates the orders as well

#Neil you need to add all off the methodfs that I have created into your waiter class and have the functions that conduct those specific actions such as asking th party size, welcoming guests etc. 
'''Joaddan's Code'''
class MenuItem:
    def __init__(self, name, keywords): #Neil the attributes in the Waiter class need to change to match the restaurant class that I created so that they can talk to one another. 
        self.name = name               # that means they should probably be self, restaurant and menu  (menu, when Joaddan creates that class because the waiter will be talking to and referring back to the menu overall)
        self.keywords = keywords
        

class Menu:
    def __init__(self):
        # Read the CSV file
        # Use that to populate self.foods
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


"""Neil's Code """        
class Waiter:
    # Attributes
    # self.party_size (int, has the guest party size)
    # self.restaurant_tables (dictionary, set of tables in the restaurant)
    # self.menu (Menu, represent the menu in the restaurant)

    """Initializes a class called waiter who assigns guests to the corresponding table"""
    def __init__(self, restaurant_tables):
        self.restaurant_tables = restaurant_tables
        self.party_size = 0
        self.menu = Menu()

    def take_order(self):
        # get order from user
        # Use the self.menu to find the order
        self.menu.display_menu()
        self.menu.find_food(order)

    def welcome_guest(self):
        print(f"Great, we have a nice table for {self.party_size} guests! Right this way please!")
    
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
        print(f'Ordering for party of {party_size} ({person}):')
        orders[person] = []
        for i in range(party_size):
            print(f'Ordering for person {i+1}:')
            order = input('What would you like to eat today? ')
            matches = menu.find_food(order)
            if matches:
                print(f'Menu items matching "{order}":')
                for match in matches:
                    print(match.name)
                waiter = input("Please choose an item you would like to eat: ")
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
            if item:
                for food in menu.foods:
                    if item == food.name:
                        total_price += food.price
                        break
        bill[person] = total_price
    return bill



def main():
    waiter = Waiter(restaurant_tables)
    restauran_t = Restaurant("J.J.K.N Grill & Buffet", waiter)

    restauran_t.welcome_guest() 
    restauran_t.ask_party_size()    # This is going to set the party size attribute in waiter

    restauran_t.ask_waiter_to_serve()

    print("Thank you for dining in our restaurant!")
if __name__ =="__main__":
    main()
   





