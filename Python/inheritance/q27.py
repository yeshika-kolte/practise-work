'''27. Transport Fare System

Abstract:

Transport

Derived:

Train
Flight
Bus

Implement ticket pricing.'''

from abc import *
class Transport(ABC):
    
    @abstractmethod
    def ticket_price(self):
        pass

class Train(Transport):

    def ticket_price(self):
        print("Price of Train Ticket :1000 Rs")
        
class Flight(Transport):

    def ticket_price(self):
        print("Price of Flight Ticket :5000 Rs")
        
class Bus(Transport):

    def ticket_price(self):
        print("Price of Bus Ticket :500 Rs")
        


train = Train()
train.ticket_price()

flight = Flight()
flight.ticket_price()

bus = Bus()
bus.ticket_price()
