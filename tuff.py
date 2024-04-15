
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
>>>>>>> fdc6eb9b81c2c9646f7acf2e8ecb89e3779a89fd
