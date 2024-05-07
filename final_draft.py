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
