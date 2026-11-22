'''

10. Movie Ticket Booking

Parent:

Ticket

Derived:

GoldTicket
PlatinumTicket
VIPTicket

Apply pricing logic.
'''
class Ticket:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def ticket(self):
        pass

class Gold_Ticket(Ticket):
    
    def ticket(self):
        if self.get_price() >= 500 and self.get_price() <1000:
            print("Gold Ticket")
    
class Platinum_Ticket(Ticket):

    def ticket(self):
        if self.get_price()>=1000 and self.get_price() <1500:
            print("Platinum Ticket")
    
class VIP_Ticket(Ticket):

    def ticket(self):
        if self.get_price()>=2000 and self.get_price() <5000:
            print("VIP Ticket")


obj1 = Gold_Ticket(600)
obj1.ticket()

obj2 = Platinum_Ticket(1200)
obj2.ticket()

obj3 = VIP_Ticket(2300)
obj3.ticket()

