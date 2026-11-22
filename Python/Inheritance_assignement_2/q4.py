'''4. Vehicle Parking Fee System
Problem Statement

Parking fees vary by vehicle type.

Create:

abstract class Vehicle

Child classes:

Bike
Car
Bus

Rules:

Bike → ₹10/hour
Car → ₹30/hour
Bus → ₹50/hour'''

from abc import *

class Vehicle(ABC):

    @abstractmethod
    def parking_fee(self):
        pass


class Bike(Vehicle):

    def __init__(self, hours):
        self.__hours = hours

    def parking_fee(self):
        
        print(f"Bike Parking Fee : Rs {self.__hours * 10}")


class Car(Vehicle):

    def __init__(self, hours):
        self.hours = hours

    def parking_fee(self):
        
        print(f"Car Parking Fee : Rs {self.__hours * 30}")



class Bus(Vehicle):

    def __init__(self, hours):
        self.hours = hours

    def parking_fee(self):
        fee = self.hours * 50
        print(f"Bus Parking Fee : Rs {self.__hours * 50}")


b1 = Bike(2)
b1.parking_fee()
c1 = Car(3)
c1.parking_fee()
bs1 = Bus(4)
bs1.parking_fee()