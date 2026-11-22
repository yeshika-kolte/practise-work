'''
Abstract:

Ride

Derived:

BikeRide
CabRide
AutoRide

Calculate fare.'''

from abc import *

class Ride(ABC):
    @abstractmethod
    def fare(self):
        pass

class BikeRide(Ride):

    __ride_per_km = 10

    def __init__(self):
        self.__distance = int(input("Enter the distance"))

    def fare(self):
        print("Bike Ride")
        print(f"Riding Fare : Rs{self.__distance *BikeRide.__ride_per_km }")



class CabRide(Ride):
    
    __ride_per_km = 100

    def __init__(self):
        self.__distance = int(input("Enter the distance"))
    def fare(self):
        
        print("Cab Ride")
        print(f"Riding Fare : Rs {self.__distance *CabRide.__ride_per_km }")



class AutoRide(Ride):
    __ride_per_km = 60
    def __init__(self):
        self.__distance = int(input("Enter the distance"))

    def fare(self):
        print("Auto Ride")
        print(f"Riding Fare : Rs {self.__distance *AutoRide.__ride_per_km }")


obj = None
print("Choose 1 from Bike Ride")
print("Choose 2 for Cab Ride")
print("Choose 3 for Auto Ride")

choice = int(input("Enter choice"))

if choice == 1:
    obj = BikeRide()
    obj.fare()
elif choice == 2:
    obj = CabRide()
    obj.fare()

else:
    obj = AutoRide()
    obj.fare()