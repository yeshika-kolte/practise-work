from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPal(Payment):
    def pay(self):
        print("Payment done using PayPal")

class Stripe(Payment):
    def pay(self):
        print("Payment done using Stripe")

class Razorpay(Payment):
    def pay(self):
        print("Payment done using Razorpay")


obj1 = PayPal()
obj1.pay()
obj2 = Stripe()
obj2.pay()
obj3 = Razorpay()
obj3.pay()