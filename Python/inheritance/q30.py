'''30. Restaurant Management

Abstract:

Restaurant

Derived:

PizzaRestaurant
BurgerRestaurant

Prepare food differently.
'''

from abc import ABC, abstractmethod

class Restaurant(ABC):

    @abstractmethod
    def prepare_food(self):
        pass


class PizzaRestaurant(Restaurant):

    def prepare_food(self):
        print("Preparing Pizza with cheese, sauce, and toppings")


class BurgerRestaurant(Restaurant):

    def prepare_food(self):
        print("Preparing Burger with bun, patty, and vegetables")


p1 = PizzaRestaurant()
b1 = BurgerRestaurant()

p1.prepare_food()
b1.prepare_food()