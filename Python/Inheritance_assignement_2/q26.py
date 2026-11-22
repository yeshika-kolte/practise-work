from abc import ABC, abstractmethod

class WaterBill(ABC):
    @abstractmethod
    def calculate_bill(self, units):
        pass

class Residential(WaterBill):
    def calculate_bill(self, units):
        bill = units * 5
        print(f"Residential Bill : {bill}")

class Commercial(WaterBill):
    def calculate_bill(self, units):
        bill = units * 10
        print(f"Commercial Bill : {bill}")

class Agricultural(WaterBill):
    def calculate_bill(self, units):
        bill = units * 2
        print(f"Agricultural Bill : {bill}")

obj1 = Residential()
obj1.calculate_bill(100)

obj2 = Commercial()
obj2.calculate_bill(100)

obj3 = Agricultural()
obj3.calculate_bill(100)