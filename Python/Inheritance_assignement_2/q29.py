from abc import ABC, abstractmethod

class Insurance(ABC):
    @abstractmethod
    def calculate_premium(self):
        pass

class HealthInsurance(Insurance):
    def calculate_premium(self):
        print("Health Insurance Premium : 5000")

class CarInsurance(Insurance):
    def calculate_premium(self):
        print("Car Insurance Premium : 8000")

class LifeInsurance(Insurance):
    def calculate_premium(self):
        print("Life Insurance Premium : 12000")

obj1 = HealthInsurance()
obj1.calculate_premium()

obj2 = CarInsurance()
obj2.calculate_premium()

obj3 = LifeInsurance()
obj3.calculate_premium()