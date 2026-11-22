'''3. Employee Management

Base class Employee.

Derived:

Developer
Tester
HR

Calculate salaries differently.'''
class Employee:
    def __init__(self, name , salary):
        self.__name = name
        self.__salary = salary

    def total_salary(self):
        return self.__salary
    
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary

class Developer(Employee):
    def total_salary(self):
        print(f"Total Salary of {self.get_name()}: {self.get_salary()}")
        

class Tester(Employee):
    def total_salary(self):
        print(f"Total Salary of {self.get_name()}: {self.get_salary()}")

class Hr(Employee):
    def total_salary(self):
        print(f"Total Salary of {self.get_name()}: {self.get_salary()}")

obj1 = Developer("Rahul", 20000)
obj1.total_salary()
obj2 = Tester("Riya", 27000)
obj2.total_salary()
obj3 = Hr("Adesh", 65000)
obj3.total_salary()