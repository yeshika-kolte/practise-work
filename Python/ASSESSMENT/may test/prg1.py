# Question 1 — Inheritance and Method Overriding

# Create a class Employee with the following:

# Instance variables:
# name
# salary
# Method:
# display_details()

# Create a child class Manager that inherits from Employee.

# Additional requirements for Manager:

# Add one extra variable department
# Override the display_details() method to display all details including department.
# Expected Output Example
# Name: Rahul
# Salary: 50000
# Department: HR

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):  
        print(f"Name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"department:{self.department}")

m1 = Manager("Rahul", 50000, "HR")
m1.display_details()              