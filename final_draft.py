class Restaurant: 
    def __init__(self,name):
        self.name = name 
        self.waiter = Waiter()

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
