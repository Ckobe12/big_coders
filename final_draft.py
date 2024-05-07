hello ne wcode 

"""Neil's Code """ 
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