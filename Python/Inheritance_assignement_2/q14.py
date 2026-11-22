'''14. Employee Attendance Tracker
Problem Statement

Attendance calculation differs.

Create:

abstract class Employee

Child:

FullTimeEmployee
PartTimeEmployee
ContractEmployee'''


from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def attendance(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, days_present):
        self.days_present = days_present

    def attendance(self):
        print(f"Full Time Employee Attendance: {self.days_present} days")


class PartTimeEmployee(Employee):

    def __init__(self, hours_worked):
        self.hours_worked = hours_worked

    def attendance(self):
        print(f"Part Time Employee Attendance: {self.hours_worked} hours")


class ContractEmployee(Employee):

    def __init__(self, working_days):
        self.working_days = working_days

    def attendance(self):
        print(f"Contract Employee Attendance: {self.working_days} days")


f = FullTimeEmployee(25)
p = PartTimeEmployee(120)
c = ContractEmployee(20)

f.attendance()
p.attendance()
c.attendance()