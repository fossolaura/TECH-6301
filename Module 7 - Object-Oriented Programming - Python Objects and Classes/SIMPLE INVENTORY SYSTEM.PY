#Requirements

#Create a simple inventory system that manages information about products 
#in a store. Each product should have specified attributes like name, price, 
#and quantity. Use classes to represent products and include methods for displaying 
#product information, updating quantities, and calculating the total value of the inventory.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def update_quantity(self, amount, is_sold=False):
        if is_sold:
            self.quantity -= amount
        else:
            self.quantity += amount

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"{name} added to the inventory.")

    def display_inventory(self):
        print("\nInventory:")
        for product in self.products:
            product.display_product_info()
        print(f"Total Inventory Value: ${self.calculate_total_value():.2f}")

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value

def main():
    inventory = Inventory()
    
    # Adding new products to the inventory
    inventory.add_product("Macbook M2", 1200, 5)
    inventory.add_product("IPhone 15", 800, 10)
    inventory.add_product("Ipad Pro", 600, 8)
    inventory.add_product("Ipad Mini", 60, 5)
    inventory.add_product("Ipod Touch", 900, 2)
    inventory.add_product("Apple Pen", 1000, 9)

    # Displaying the inventory
    inventory.display_inventory()

    # Updating the quantity of a product
    print("\nSelling 2 IPad Mini...")
    inventory.products[3].update_quantity(2, is_sold=True)
    print("\nSelling 3 Macbook M2...")
    inventory.products[0].update_quantity(3, is_sold=True)
    print("\nSelling 5 Apple Pen...")
    inventory.products[5].update_quantity(5, is_sold=True)
    
    # Displaying the inventory after update
    inventory.display_inventory()

if __name__ == "__main__":
    main()
