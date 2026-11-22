# 8. Online Food Delivery
# Parent:
# FoodItem
# Derived:
# Pizza
# Burger
# Sandwich
# Calculate total bill.

from abc import abstractmethod,ABC
class Food(ABC):
    def _init_(self, price, quantity):
        self.__price=price
        self.__quantity=quantity
        
    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity
    
    @abstractmethod  
    def display(self):
        pass
    
class Pizza(Food):
    def display(self):
        total = self.get_price() * self.get_quantity()
        print("Pizza")
        print("Price :", self.get_price())
        print("Quantity :", self.get_quantity())
        print("Total Bill :", total)
        
class Burger(Food):
    def display(self):
        total = self.get_price() * self.get_quantity()
        print("Burger")
        print("Price :", self.get_price())
        print("Quantity :", self.get_quantity())
        print("Total Bill :", total)
        
class Sandwich(Food):
    def display(self):
        total = self.get_price() * self.get_quantity()
        print("Sandwich")
        print("Price :", self.get_price())
        print("Quantity :", self.get_quantity())
        print("Total Bill :", total)
        
P1=Pizza(200, 2)
P1.display()

P2=Burger(80, 5)
P2.display()

P3=Sandwich(50, 4)
P3.display()