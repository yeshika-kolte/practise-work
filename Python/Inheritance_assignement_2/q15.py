from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Payment of {amount} using Credit Card")

class DebitCard(Payment):

    def process_payment(self, amount):
        print(f"Payment of {amount} using Debit Card")

class UPI(Payment):
    def process_payment(self, amount):
        print(f"Payment of {amount} using UPI")


obj1 = CreditCard()
obj1.process_payment(5000)

obj2 = DebitCard()
obj2.process_payment(3000)

obj3 = UPI()
obj3.process_payment(1500)