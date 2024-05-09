import csv 

"""Joaddan Cadet"""
class MenuItem:
     """
   Initialize a MenuItem object.


   Args:
       name (str): The name of the menu item.
       price (float): Price that goes with the menu item.
   """

    
     def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
     """
   Represents a menu containing multiple MenuItem things.
   """

     def __init__(self):
            self.foods = []

     def add_food(self, food):
          """
       Adds a MenuItem to the menu.


       Args:
           Food (MenuItem): The MenuItem is added to the menu.
       """
          self.foods.append(food)

     def display_menu(self):
         """
       Displays the menu by printing each MenuItem's name and price.
       """
         print("Menu:")
         for food in self.foods:
             print(f"{food.name}: ${food.price}")

     def find_food(self, keyword):
         """
       Finds MenuItem whose names contain the keyword.


       Args:
           keyword (str): This represents the keyword to search for in menu item.


       Returns:
           list: A list of MenuItem that matches the keyword.
       """

         matches = []
         for food in self.foods:
            if keyword.lower() in food.name.lower():
                matches.append(food)
         return matches

     def read_menu_from_csv(self, file_path):
         
         """
      This reads menu items from CSV file and adds them to the menu.


       Args:
           file_path (str): The path to the CSV file that contains the menu.
       """
         with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Item']
                    price = float(row['Price'].replace('$', '').strip())
                    food = MenuItem(name, price)
                    self.add_food(food)
class Restaurant:
    def __init__(self, name= "Whatever you want", waiter = None):
        self.name = name
        self.waiter = waiter

    def welcome_guest(self):
        print(f"Welcome to {self.name}!")

    def ask_party_size(self):
        self.waiter.party_size = int(input("How many guests are in your party today?"))

    def ask_waiter_to_serve(self):
        self.waiter.assign_guests(self.waiter.party_size)
    
    
    
    def book_table(self, table_number):
        if table_number in self.waiter.restaurant_tables:
            if self.waiter.restaurant_tables[table_number] >0:
                print(f"Table {table_number} has been reserved.")
                self.waiter.restaurant_tables[table_number] = 0 
            else:
                print(f"sorry, table{table_number} is not available.")
        else:
             print("Invalid table number.")
     
    def __str__(self):
        return f"Restaurant: {self.name}, Waiter: {self.waiter}"