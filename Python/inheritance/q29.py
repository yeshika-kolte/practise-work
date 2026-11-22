'''29. Employee Attendance

Abstract:

Employee

Derived:

FullTimeEmployee
PartTimeEmployee

Calculate working hours.
'''

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def working_hours(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, hours):
        self.hours = hours

    def working_hours(self):
        print(f"Full Time Employee Working Hours: {self.hours} hours per day")



class PartTimeEmployee(Employee):

    def __init__(self, hours):
        self.hours = hours

    def working_hours(self):
        print(f"Part Time Employee Working Hours: {self.hours} hours per day")


f1 = FullTimeEmployee(8)
f1.working_hours()
p1 = PartTimeEmployee(4)
p1.working_hours()