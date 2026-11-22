# 7. Cab Fare Calculator
# Problem Statement

# Cab fares differ based on ride type.

# Create:

# abstract class Ride

# Child:

# MiniRide
# SedanRide
# SUVRide

# Rules:

# Mini → ₹10/km
# Sedan → ₹15/km
# SUV → ₹20/km

from abc import ABC, abstractmethod


class Ride(ABC):

    @abstractmethod
    def calculate_fare(self):
        pass


class MiniRide(Ride):

    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        fare = self.distance * 10
        print(f"Mini Ride Fare : Rs {fare}")


class SedanRide(Ride):

    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        fare = self.distance * 15
        print(f"Sedan Ride Fare : Rs {fare}")


class SUVRide(Ride):

    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        fare = self.distance * 20
        print(f"SUV Ride Fare : Rs {fare}")



m1 = MiniRide(5)
s1 = SedanRide(5)
u1 = SUVRide(5)

m1.calculate_fare()
s1.calculate_fare()
u1.calculate_fare()