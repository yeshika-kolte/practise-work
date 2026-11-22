from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def ticket_price(self):
        pass

class SilverTicket(Ticket):
    def ticket_price(self):
        print("Silver Ticket Price : 300")

class GoldTicket(Ticket):
    def ticket_price(self):
        print("Gold Ticket Price : 600")

class PlatinumTicket(Ticket):
    def ticket_price(self):
        print("Platinum Ticket Price : 1000")


obj1 = SilverTicket()
obj1.ticket_price()

obj2 = GoldTicket()
obj2.ticket_price()

obj3 = PlatinumTicket()
obj3.ticket_price()