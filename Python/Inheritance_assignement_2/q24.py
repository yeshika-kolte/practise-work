from abc import ABC, abstractmethod

class RidePricing(ABC):
    @abstractmethod
    def calculate_fare(self, amount):
        pass

class NormalTime(RidePricing):
    def calculate_fare(self, amount):
        fare = amount
        print(f"Normal Time Fare : {fare}")

class PeakTime(RidePricing):
    def calculate_fare(self, amount):
        fare = amount + 100
        print(f"Peak Time Fare : {fare}")

class RainTime(RidePricing):
    def calculate_fare(self, amount):
        fare = amount + 200
        print(f"Rain Time Fare : {fare}")

obj1 = NormalTime()
obj1.calculate_fare(500)

obj2 = PeakTime()
obj2.calculate_fare(500)

obj3 = RainTime()
obj3.calculate_fare(500)