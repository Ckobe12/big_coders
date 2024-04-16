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
