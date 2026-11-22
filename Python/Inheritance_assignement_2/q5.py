'''5. Online Shopping Discount System
Problem Statement

Different customer types receive different discounts.

Create:

abstract class Customer

Child:

RegularCustomer
PremiumCustomer
VIPCustomer

Rules:

Regular → 5%
Premium → 10%
VIP → 20%'''


from abc import *

class Customer(ABC):
    def __init__(self,name,id,purchase_amount):
        self.__name = name
        self.__id = id
        self.__amount = purchase_amount

    def get_amount(self):
        return self.__amount
    
    def discount(self):
        pass


class RegularCustomer(Customer):
    def discount(self):

        self.__discount = (self.get_amount() * 5 )/100
        print("---------------Regular Customer------------------")
        print(f"Total Price : {self.get_amount()}")
        print(f"Discount : {self.__discount}")
        print(f"Final Price : {self.get_amount() - self.__discount}")

class PremiuimCustomer(Customer):
    def discount(self):
        self.__discount = (self.get_amount() * 10 )/100
        print("---------------Premiuim Customer------------------")
        print(f"Total Price : {self.get_amount()}")
        print(f"Discount : {self.__discount}")
        print(f"Final Price : {self.get_amount() - self.__discount}")

class VIPCustomer(Customer):
    def discount(self):
        self.__discount = (self.get_amount() * 20 )/100
        print("---------------VIP Customer------------------")
        print(f"Total Price : {self.get_amount()}")
        print(f"Discount : {self.__discount}")
        print(f"Final Price : {self.get_amount() - self.__discount}")


rc = RegularCustomer("Rahul",212,15000)
rc.discount()

pr = PremiuimCustomer("Mukesh",231,19000)
pr.discount()

vip = VIPCustomer("Ayush",1212,40000)
vip.discount()