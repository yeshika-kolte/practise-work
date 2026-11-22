from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartFan(SmartDevice):
    def turn_on(self):
        print("Fan ON")

    def turn_off(self):
        print("Fan OFF")

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light ON")

    def turn_off(self):
        print("Light OFF")

class SmartAC(SmartDevice):
    def turn_on(self):
        print("AC ON")

    def turn_off(self):
        print("AC OFF")


obj1 = SmartFan()
obj1.turn_on()
obj1.turn_off()
obj2 = SmartLight()
obj2.turn_on()
obj2.turn_off()
obj3 = SmartAC()
obj3.turn_on()
obj3.turn_off()