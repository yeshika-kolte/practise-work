'''22. Payment Gateway

Abstract class Payment.

Derived:

CreditCard
UPI
Wallet

Implement payment processing.'''

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass

class CreditCard(Payment):

    def __init__(self, card_holder, amount):
        self.card_holder = card_holder
        self.amount = amount

    def process_payment(self):
        print(f"Credit Card payment of ₹{self.amount} processed for {self.card_holder}")


class UPI(Payment):

    def __init__(self, upi_id, amount):
        self.upi_id = upi_id
        self.amount = amount

    def process_payment(self):
        print(f"UPI payment of ₹{self.amount} processed using {self.upi_id}")


class Wallet(Payment):

    def __init__(self, wallet_name, amount):
        self.wallet_name = wallet_name
        self.amount = amount

    def process_payment(self):
        print(f"Wallet payment of ₹{self.amount} processed through {self.wallet_name}")

c1 = CreditCard("Amit", 5000)
u1 = UPI("amit@upi", 2000)
w1 = Wallet("Paytm", 1000)

c1.process_payment()
u1.process_payment()
w1.process_payment()