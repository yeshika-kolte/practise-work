class Stock:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

class Supplier:
    def __init__(self, supplier):
        self.__supplier = supplier

    def get_supplier(self):
        return self.__supplier

class Billing:
    def __init__(self, stock, price):
        self.__stock = stock
        self.__price = price

    def total_bill(self):
        return self.__stock.get_quantity() * self.__price

    def display_bill(self):
        print(f"Product : {self.__stock.get_product()}")
        print(f"Quantity : {self.__stock.get_quantity()}")
        print(f"Total Bill : {self.total_bill()}")


obj1 = Stock("Laptop", 2)
obj2 = Supplier("ABC Suppliers")
obj3 = Billing(obj1, 50000)
print(f"Supplier : {obj2.get_supplier()}")
obj3.display_bill()