#A2 cashier
# 1. make class for items
# 2. make input and save in file

class Product:
    def __init__(self, name, p_type, quantity, price):
        self.name = name
        self.type = p_type
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.type}): {self.quantity} pcs x {self.price} Baht"

import os

def storage_sys():
    storage = input('Name for create storage: ')
    full_path = os.path.abspath(f"{storage}.txt")
    print(f"Storage created at {full_path}")

    stored = False
    with open(f'{storage}.txt', 'w', encoding='utf-8') as file:
        while not stored:
            try:
                Item = input('\nName of item: ')
                Type = input('Type of item: ')
                Quantity = int(input('Quantity of item: '))
                Price = float(input('Price of item: '))
            except ValueError:
                print('Please enter valid input.')
                continue
            product = Product(Item, Type, Quantity, Price)
            file.write(f"{product}\n")
            print(f"{product} added to storage.")

            choice = input('Continue store anything? (Y/N): ').strip().lower()
            if choice == 'y':
                print('Continue store items...')
                stored = False
            elif choice != 'y':
                print('Done stored items. Ready for selling.')
                stored = True
                break

storage_sys()
