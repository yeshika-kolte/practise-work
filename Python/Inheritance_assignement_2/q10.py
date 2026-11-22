'''10. Loan Interest Calculator
Problem Statement

Banks offer different interest rates.

Create:

abstract class Loan

Child:

HomeLoan
CarLoan
EducationLoan
Formula

Interest=
100
P×R×T'''

from abc import ABC, abstractmethod

class Loan(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


class HomeLoan(Loan):

    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def calculate_interest(self):
        interest = (self.p * self.r * self.t) / 100
        print(f"Home Loan Interest: Rs {interest}")


class CarLoan(Loan):

    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def calculate_interest(self):
        interest = (self.p * self.r * self.t) / 100
        print(f"Car Loan Interest: Rs {interest}")


class EducationLoan(Loan):

    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def calculate_interest(self):
        interest = (self.p * self.r * self.t) / 100
        print(f"Education Loan Interest: Rs {interest}")


h1 = HomeLoan(100000, 7, 5)
c1 = CarLoan(500000, 9, 3)
e1 = EducationLoan(200000, 6, 4)

h1.calculate_interest()
c1.calculate_interest()
e1.calculate_intere