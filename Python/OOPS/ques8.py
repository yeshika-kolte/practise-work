# 8. Inventory Management System
# Problem

# Create product inventory software.

# Requirements

# Each product should contain:

# product id
# product name
# quantity
# price
# Functionalities
# Add stock
# Reduce stock after purchase
# Prevent negative stock
# Calculate inventory value
# Concepts Practiced
# arithmetic inside classes
# validations
# inventory logic

class product:
    def __init__(self, product_id, product_name, quantity , price):
        self.__product_id = product_id
        self.__product_name= product_name
        self.__quantity = quantity
        self.__price = price
    def add_stock(self, amount):
        self.__quantity += amount
    def reduce_stock(self, amount):
        if self.__quantity - amount >= 0:
            self.__quantity -= amount
        else:
            print("Cannot reduce stock. Not enough quantity available.")
    def calculate_value(self):
        return self.__quantity * self.__price
p1 = product("101", "Laptop", 10, 1000)
p1.add_stock(5)
p1.reduce_stock(3)
print(f"Inventory Value: {p1.calculate_value()}")
