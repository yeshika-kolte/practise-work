# Online Shopping Cart
# Problem

# Create a shopping cart system.

# Requirements

# A cart should:

# store customer name
# maintain list of products
# maintain total bill
# Functionalities
# Add product
# Remove product
# Calculate final amount
# Apply discount  using static method
# Track total carts created
# Concepts Practiced
# list inside object
# object interaction
# static method
# class variable


class cart:
    total_carts = 0
    
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.products = []
        self.total_bill = 0
        cart.total_carts += 1

    def add_product(self, product, price, quantity):
        self.products.append((product, price, quantity))
        self.total_bill += price * quantity

    def remove_product(self, product):
        for item in self.products:
            if item[0] == product:
                self.total_bill -= item[1] * item[2]
                self.products.remove(item)
                break

    def calculate_final_amount(self):
        return self.total_bill

    @staticmethod
    def apply_discount(amount, discount_rate):
        return amount - (amount * discount_rate)

cart1 = cart("yeshika")
cart1.add_product("Laptop", 1000, 1)
cart1.add_product("Mouse", 50, 2)
cart1.remove_product("Mouse")
final_amount = cart1.calculate_final_amount()
discounted_amount = cart.apply_discount(final_amount, 0.1)
print(f"Final Amount after discount: {discounted_amount}")
print("Total Carts Created:", cart.total_carts)
