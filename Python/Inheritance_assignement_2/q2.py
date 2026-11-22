'''2. Delivery Charge Calculator
Problem Statement

A delivery company calculates delivery charges differently.

Create:

abstract class Delivery

Child classes:

BikeDelivery
TruckDelivery
DroneDelivery

Rules:

Bike → ₹5/km
Truck → ₹15/km
Drone → ₹20/km
Input Example

Distance = 10 km

Expected Output
Bike Delivery Charge = 50
Truck Delivery Charge = 150'''

from abc import *
class Delivery(ABC):
    
    __distance = int(input("Enter Distance"))
    
    def get_distance(self):
        return Delivery.__distance
    @abstractmethod
    def charge(self):
        pass

class BikeDelivery(Delivery):
    def charge(self):
        print(f"Bike Delivery Charge = Rs{self.get_distance() * 5}/km")


class TruckDelivery(Delivery):
    def charge(self):
        print(f"Truck Delivery Charge = Rs{self.get_distance() * 15}/km")
    

class DroneDelivery(Delivery):
    def charge(self):
        print(f"Drone Delivery Charge = Rs{self.get_distance() * 20}/km")


bike = BikeDelivery()
bike.charge()

truck = TruckDelivery()
truck.charge()

drone = DroneDelivery()
drone.charge()