# 2. Vehicle System

# Create parent class Vehicle.

# Child classes:

# Car
# Bike
# Bus

# Add methods:

# start()
# stop()


class Vehicle:
    def start(self):
        pass

    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        return "car started"
    def stop(self):
        return "car stopped"
class Bike(Vehicle):
    def start(self):
        return "bike started"
    def stop(self):
        return "bike stopped"   
class Bus(Vehicle):
    def start(self):
        return "bus started"
    def stop(self):
        return "bus stopped"
car = Car()
bike = Bike()
bus = Bus()

print(car.start())
print(car.stop())
print(bike.start())
print(bike.stop())
print(bus.start())
print(bus.stop())
    