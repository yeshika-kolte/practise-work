# 3. Employee Management

# Base class Employee.

# Derived:

# Developer
# Tester
# HR

# Calculate salaries differently.

class Employee:
    def __init__(self, id , name ):
        self.__id = id
        self.__name = name  

    def salary(self,amount):
        return f"Employee salary: {amount}"
class Developer(Employee):
    def salary(self,amount):
        return f"Developer salary: {amount}"    

class Tester(Employee):
    def salary(self,amount):
        return f"Tester salary: {amount}"
class HR(Employee):
    def salary(self,amount):
        return f"HR salary: {amount}"

dev = Developer(1,"Amit")
tester = Tester(2,"Rahul")
hr = HR(3,"Priya")

print(dev.salary(50000))
print(tester.salary(40000))
print(hr.salary(45000))