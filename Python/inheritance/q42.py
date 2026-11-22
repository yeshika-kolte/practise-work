from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    def display_product(self):
        print(f"Product : {self.get_name()}")
        print(f"Price : {self.get_price()}")

class Order:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product
    
    def get_quantity(self):
        return self.__quantity

    def total_amount(self):
        return self.get_product().get_price() * self.get_quantity()

    def display_order(self):
        print(f"Ordered Product : {self.get_product().get_name()}")
        print(f"Quantity : {self.get_quantity()}")
        print(f"Total Amount : {self.total_amount()}")

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Amt{amount} using UPI")

class CashOnDelivery(Payment):
    def pay(self, amount):
        print(f"Amt {amount} COD")

class Delivery:
    def __init__(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def deliver(self):
        print(f"Order delivery : {self.get_address()}")

p1 = Product("Laptop", 50000)
o1 = Order(p1, 2)
pay1 = UPI()
d1 = Delivery("Bhopal")
p1.display_product()
o1.display_order()
pay1.pay(o1.total_amount())
d1.deliver()