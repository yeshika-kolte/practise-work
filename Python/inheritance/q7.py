'''7. Shopping Cart System

Base:

Product

Derived:

Electronics
Grocery
Clothing

Apply discounts.'''

class Product():
    def __init__(self,name,price):
        self.__name=name
        self.__price = price

    def discount(self, percent):
        pass

    def get_price(self):
        return self.__price
    def get_name(self):
        return self.__name
    
class Electronic(Product):
    def discount(self, percent):
        final_price = (self.get_price()* percent)/100
        print(f"Product Name :{self.get_name()}")
        print(f"Total Amt {final_price}")

        
class Grocery(Product):
    def discount(self, percent):
        final_price = (self.get_price()* percent)/100
        print(f"Product Name :{self.get_name()}")
        print(f"Total Amt {final_price}")

        
class Clothing(Product):
    def discount(self, percent):
        final_price = (self.get_price()* percent)/100
        print(f"Product Name :{self.get_name()}")
        print(f"Total Amt {final_price}")

obj1= Electronic("Mobile", 14000)
obj1.discount(2)
obj2= Grocery("Broom", 500)
obj2.discount(10)
obj3= Clothing("Shirt", 1000)
obj3.discount(5)