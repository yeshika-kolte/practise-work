'''9. Food Billing System
Problem Statement

Restaurants apply different GST percentages.

Create:

abstract class FoodItem

Child:

VegFood
NonVegFood
Beverage

Rules:

Veg → 5%
NonVeg → 12%
Beverage → 18%'''

from abc import ABC, abstractmethod

class FoodItem(ABC):

    @abstractmethod
    def bill(self):
        pass


class VegFood(FoodItem):

    def __init__(self, price):
        self.price = price

    def bill(self):
        total = self.price + (self.price * 0.05)
        print(f"Veg Food Bill: Rs {total}")


class NonVegFood(FoodItem):

    def __init__(self, price):
        self.price = price

    def bill(self):
        total = self.price + (self.price * 0.12)
        print(f"NonVeg Food Bill: Rs {total}")


class Beverage(FoodItem):

    def __init__(self, price):
        self.price = price

    def bill(self):
        total = self.price + (self.price * 0.18)
        print(f"Beverage Bill: Rs {total}")


v1 = VegFood(200)
n1 = NonVegFood(300)
b1 = Beverage(100)

v1.bill()
n1.bill()
b1.bill()