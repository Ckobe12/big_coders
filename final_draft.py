import csv 
import argparse

"""Joaddan Cadet"""
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.foods = []

    def add_food(self, food):
        self.foods.append(food)

    def display_menu(self):
        print("Menu:")
        for food in self.foods:
            print(f"{food.name}: ${food.price}")

    def find_food(self, keyword):
        matches = []
        for food in self.foods:
            if keyword.lower() in food.name.lower():
                matches.append(food)
        return matches

    def read_menu_from_csv(self, file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Item']
                price = float(row['Price'].replace('$', '').strip())
                food = MenuItem(name, price)
                self.add_food(food)
"""Kobe's Code"""
class Restaurant:
    def __init__(self, name, waiter):
        self.name = name
        self.waiter = waiter

    def welcome_guest(self):
        print(f"Welcome to {self.name}!")

    def ask_party_size(self):
        self.waiter.party_size = int(input("How many guests are in your party today?"))

    def ask_waiter_to_serve(self):
        self.waiter.assign_guests(self.waiter.party_size)

'''Neil's Code'''

class Waiter:
    def __init__(self, restaurant_tables):
        self.restaurant_tables = restaurant_tables
        self.party_size = 0
        self.menu = Menu()

    def assign_guests(self, num_guests):
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
    bill = {}
    sorted_menu = sorted(menu.foods, key=lambda x: x.price)
    for person, order_list in orders.items():
        total_price = 0
        for item in order_list:
            if item:
                for food in sorted_menu:
                    if item == food.name:
                        total_price += food.price
                        break
        bill[person] = total_price
    return bill

def main():
     # Create an instance of the Waiter class
    waiter = Waiter(restaurant_tables)
    
    
    
    
    
    
if __name__ == "__main__":
    main()