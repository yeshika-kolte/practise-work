'''2. Vehicle System

Create parent class Vehicle.

Child classes:

Car
Bike
Bus

Add methods:

start()
stop()'''

from abc import *

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car Start")

    def stop(self):
        print("Car Stop")

class Bike(Vehicle):
    def start(self):
        print("Bike Start")

    def stop(self):
        print("Bike stop")

class Bus(Vehicle):
    def start(self):
        print("Bus Start")

    def stop(self):
        print("Bus stop")


car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()

bus = Bus()

bus.start()
bus.stop()