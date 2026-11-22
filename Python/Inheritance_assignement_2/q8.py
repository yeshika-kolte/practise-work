'''8. Salary Tax Calculator
Problem Statement

Tax calculation differs by employee category.

Create:

abstract class TaxPayer

Child:

GovernmentEmployee
PrivateEmployee
Freelancer'''

from abc import ABC, abstractmethod

class TaxPayer(ABC):

    @abstractmethod
    def calculate_tax(self):
        pass


class GovernmentEmployee(TaxPayer):

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax(self):
        tax = self.salary * 0.05
        print(f"Government Employee Tax : Rs {tax}")


class PrivateEmployee(TaxPayer):

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax(self):
        tax = self.salary * 0.10
        print(f"Private Employee Tax : Rs {tax}")


class Freelancer(TaxPayer):

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax(self):
        tax = self.salary * 0.15
        print(f"Freelancer Tax : Rs {tax}")


g1 = GovernmentEmployee(50000)
p1 = PrivateEmployee(50000)
f1 = Freelancer(50000)

g1.calculate_tax()
p1.calculate_tax()
f1.calculate_tax()