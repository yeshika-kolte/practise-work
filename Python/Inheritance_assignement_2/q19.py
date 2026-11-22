from abc import ABC, abstractmethod

class Courier(ABC):
    @abstractmethod
    def price(self, weight):
        pass

class NormalCourier(Courier):
    def price(self, weight):
        price = weight * 50
        print(f"Normal Courier Price : {price}")

class ExpressCourier(Courier):
    def price(self, weight):
        price = weight * 100
        print(f"Express Courier Price : {price}")

class SameDayCourier(Courier):
    def price(self, weight):
        price = weight * 150
        print(f"Same Day Courier Price : {price}")

obj1 = NormalCourier()
obj1.price(2)

obj2 = ExpressCourier()
obj2.price(2)

obj3 = SameDayCourier()
obj3.price(2)