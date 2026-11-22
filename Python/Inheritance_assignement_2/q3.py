'''
3. Electricity Bill Generator
Problem Statement

Electricity bills are calculated differently for:

Residential users
Commercial users
Industrial users

Create abstract class ElectricityBill.

Rules

Residential:

Bill=Units×5

Commercial:

Bill=Units×8

Industrial:

Bill=Units×12

Concepts
Runtime polymorphism
Real-world billing logic'''

from abc import *

class ElectricityBill(ABC):
    
    @abstractmethod
    def calculate_bill(self):
        pass


class ResidentialUser(ElectricityBill):
    def __init__(self,unit):
        self.__unit = unit
    
    def calculate_bill(self):
        print(f"Total Bill in Resdential :{self.__unit * 5 } ")


class CommercialUser(ElectricityBill):
    def __init__(self,unit):
        self.__unit = unit
    
    def calculate_bill(self):
        print(f"Total Bill in Commercial :{self.__unit * 8} ")

class IndustrialUser(ElectricityBill):
    def __init__(self,unit):
        self.__unit = unit
    
    def calculate_bill(self):
        print(f"Total Bill in Industry :{self.__unit * 12} ")


res=ResidentialUser(10)
res.calculate_bill()

cm=CommercialUser(12)
cm.calculate_bill()

ind = IndustrialUser(20)
ind.calculate_bill()
