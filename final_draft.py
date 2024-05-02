""" Kobe's Code"""
class Restaurant: 
    def __init__(self,name, waiter = None):
        self.name = name 
        
    def welcome_guest(self):
        print(f"Welcome to {self.name}!")
    
    def ask_party_size(self): 
        return int(input("How many guests are in your party today?"))
    
def main():
        restauran_t = Restaurant("J.J.K.N Grill & Buffet")
        restauran_t.welcome_guest() 
        
        party_size =  restauran_t.ask_party_size()
        print(f"Great, we have a nice table for {party_size} guests! Right this way please!")
        
if __name__ =="__main__":
            main()
         

class Waiter:
   





restauran_t = Restaurant("J.J.K.N Grill & Buffet!")
restauran_t.welcome_guest()
        
        
        """Neil's Code """
        
class Waiter:
    def welcome_guest(self):
        print("Hello guests , welcom")
    
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


class Waiter: 
    def __init__(self,restaurant_tables,menu):
        self.restaurant_tables = restaurant_tables
        self.menu = menu

    def welcoming_customer(self):
        print(f"Welcome to {self.name}!")
        self.waiter.greet_customer()

class Waiter: 
    
    """ Notes from TA 

# Program start point
# if__name__ == "__main__':
# make an instance of a waiter
# waiter = Waiter(restaurant_tables))
# 
# 
# # waiter greets the customer 
# waiter determines the right table and seats them 
# Method in a waiter object
# 
# Waiter displays the menu to user
# user sees the menu, and orders
# 
# Waiter calculates the amount needed, and shows to user 
# user inputs amount of payment
# 
# 
# Class waiter
# attributes 
# tables
# menu 
# menu items
# def__init__(self,tables) -> None:
# self.tables = """

waiter = Waiter(restaurant_tables)


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
