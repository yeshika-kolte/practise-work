from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def ticket_price(self, distance):
        pass

class Bus(Transport):
    def ticket_price(self, distance):
        fare = distance * 5
        print(f"Bus Fare : {fare}")

class Train(Transport):
    def ticket_price(self, distance):
        fare = distance * 8
        print(f"Train Fare : {fare}")

class Flight(Transport):
    def ticket_price(self, distance):
        fare = distance * 20
        print(f"Flight Fare : {fare}")

obj1 = Bus()
obj1.ticket_price(100)

obj2 = Train()
obj2.ticket_price(100)

obj3 = Flight()
obj3.ticket_price(100)