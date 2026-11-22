'''1. Employee Bonus Calculator
Problem Statement

A company gives bonuses differently based on employee type.

Create:

abstract class Employee
child classes:
Developer
Manager
Intern

Rules:

Developer → 20% bonus
Manager → 35% bonus
Intern → fixed ₹5000 bonus
Requirements

Methods:

calculate_bonus()
display_details()
Concepts
Abstract class
Method overriding
Business logic'''

from abc import *
class Employee(ABC):
    def __init__(self,name,emp_id,salary):
        self.__name = name
        self.__emp_Id = emp_id
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_empId(self):
        return self.__emp_Id
    
    def get_salary(self):
        return self.__salary
    
    @abstractmethod
    def calculate_bonus(self):
        pass
    @abstractmethod
    def display_detail(self):pass

class Developer(Employee):
    def display_detail(self):
       print("-----------------Developer Detail-------------------------")
       print(f"Developer Name : {self.get_name()}")
       print(f"Developer Id : {self.get_empId()}")
       print(f"Salary : {self.get_salary()}")

    def calculate_bonus(self):
        self.__bonus = (self.get_salary()) * 20/100
        print(f"Total Salary After Bonus : {self.get_salary() + self.__bonus}")

class Manager(Employee):
    def display_detail(self):
       print("-----------------Manager Detail-------------------------")
       print(f"Manager Name : {self.get_name()}")
       print(f"Manager Id : {self.get_empId()}")
       print(f"Salary : {self.get_salary()}")

    def calculate_bonus(self):
        self.__bonus = (self.get_salary()) * 20/100
        print(f"Total Salary After Bonus : {self.get_salary() + self.__bonus}")

class Intern(Employee):
    def display_detail(self):
       print("-----------------Intern Detail-------------------------")
       print(f"Intern Name : {self.get_name()}")
       print(f"Intern Id : {self.get_empId()}")
       print(f"Salary : {self.get_salary()}")

    def calculate_bonus(self):
        self.__bonus = 5000
        print(f"Total Salary After Bonus : {self.get_salary() + self.__bonus}")


d1 = Developer("Ayush",101,10000)
d1.display_detail()
d1.calculate_bonus()
m1 = Manager("Amit",102,130000)
m1.display_detail()
m1.calculate_bonus()
i1 = Intern("Rahul",1221,15000)
i1.display_detail()
i1.calculate_bonus()