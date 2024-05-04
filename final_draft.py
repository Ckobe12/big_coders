
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
    def __init__(self, name, keywords):
        self.name = name
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

def main():
    waiter = Waiter(restaurant_tables)
    restauran_t = Restaurant("J.J.K.N Grill & Buffet", waiter)

    restauran_t.welcome_guest() 
    restauran_t.ask_party_size()    # This is going to set the party size attribute in waiter

    restauran_t.ask_waiter_to_serve()

    print("Thank you for dining in our restaurant!")

if __name__ =="__main__":
    main()

   





