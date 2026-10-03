#A2 cashier
# 1. make class for items
# 2. make while loop for input and save in file
# 3. make selling system for items when about to sell

class Product:
    def __init__(self, name, p_type, quantity, price):
        self.name = name
        self.type = p_type
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.type}): {self.quantity} pcs x {self.price} Baht"

class PackProduct(Product):
    def __init__(self, name, p_type, quantity, price, pack_size, discount):
        super().__init__(name, p_type, quantity, price)
        self.pack_size = pack_size
        self.discount = discount
        self.pack_price = price * (1 - discount / 100)

    def __str__(self):
        return (super().__str__() + 
                f" | Pack: {self.pack_size} pcs. {self.discount:.2f}% discount: {self.pack_price:.2f} Baht/pcs")
    
import os
def storage_sys():
    storage = input('Name for create storage: ')
    full_path = os.path.abspath(f"{storage}.txt")
    print(f"Storage created at {full_path}")
    products = []
    stored = False
    with open(f'{storage}.txt', 'w', encoding='utf-8') as file:
        while not stored:
            try:
                Item = input('\nName of item: ')
                Type = input('Type of item: ')
                Quantity = int(input('Quantity of item: '))
                Price = float(input('Price of item: '))

                if Quantity < 1:
                    print('Error: Quantity must be a positive integer.')
                    continue

                if Price < 0:
                    print('Error: Price cannot be negative.')
                    continue

                sale_type = input('Type? 1.Retail only (enter 1/r) 2.Pack(can retail) (enter 2/p): ').strip().lower()

                if sale_type == '2' or sale_type == 'p':
                    pack_size = int(input('Pack size: '))
                    if pack_size < 1:
                        print('Error: Pack size must be a positive integer.')
                        continue
                    discount = float(input('Discount (%): '))

                    if discount < 0 or discount > 100:
                        print('Discount must be between 0 and 100.')
                        continue

                    product = PackProduct(Item, Type, Quantity, Price, pack_size, discount)
                elif sale_type == '1' or sale_type == 'r':
                    product = Product(Item, Type, Quantity, Price)
                else:
                    print('Invalid sale type. Please enter 1, r, 2, or p.')
                    continue

            except ValueError:
                print('Please enter valid input.')
                continue

            products.append(product)
            file.write(f"{product}\n")
            print(f"{product} added to storage.")

            choice = input('Continue store anything? (Y/N): ').strip().lower()
            if choice == 'y':
                print('Continue store items...')
                stored = False
            else:
                print('Done stored items. Ready for selling.')
                stored = True
    selling_sys(products, storage)

def selling_sys(products, storage):
    for product in products:
        if product.quantity == 0:
            print(f"\n{product.name} is out of stock.")

            choice = input(f'Restock this item? (Y/N): ').strip().lower()
            if choice == 'y':
                try:
                    amount = int(input('Restock quantity: '))
                    if amount < 1:
                        print('Error: Quantity must be a positive integer.')
                        continue
                    else:
                        product.quantity += amount
                        print(f'{product.name} restocked. Current stock: {product.quantity}')
                except ValueError:
                    print('Please enter a valid quantity(an integer).')
            else:
                print(f'No restock for {product.name}.')
                return
            
    choice = input('\nStart selling items? (Y/N): ').strip().lower()
    if choice == 'y':
        print('=' * 20 + 'Show Product list' + '=' * 20)
        for i,product in enumerate(products, start=1):
            print(f"{i}. {product}")
        print('=' * 57)
        print(f'{storage} is opened. Ready for selling.')
    else:
        print(f'{storage} is closed.')
    
storage_sys()