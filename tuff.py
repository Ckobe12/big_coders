
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



    




