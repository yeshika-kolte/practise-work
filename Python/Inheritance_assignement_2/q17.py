from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def operate(self):
        pass

class Fan(Appliance):
    def operate(self):
        print("Fan is running")

class AC(Appliance):
    def operate(self):
        print("AC is cooling")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing Machine is washing")

obj1 = Fan()
obj1.operate()

obj2 = AC()
obj2.operate()

obj3 = WashingMachine()
obj3.operate()