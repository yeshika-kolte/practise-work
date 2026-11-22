# Employee Management System
# Problem

# Create an Employee class to manage employee details.

# Requirements

# Each employee should have:

# employee id
# name
# department
# salary
# Functionalities
# Display employee details
# Increase salary by percentage
# Count total employees created using a class variable

# Create employee object from a string:

# "101-Rahul-IT-50000"

# using a class method.

# Concepts Practiced
# constructor
# instance variables
# class variables
# class method
# instance methods

class Employee:
    
    total_employees = 0

    def __init__(self, emp_id, name, department, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department
        self.__salary = int(salary)

        Employee.total_employees += 1

    
    def display_details(self):
        print(f"ID: {self.__emp_id}, Name: {self.__name}, "
              f"Department: {self.__department}, Salary: {self.__salary}")

    
    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    
    @classmethod
    def string(cls, inp_str):
        emp_id, name, department, salary = inp_str.split("-")
        return cls(emp_id, name, department, salary)



e1 = Employee(101, "Rahul", "IT", 50000)
e1.display_details()
e1.increase_salary(10)

e2 =Employee.string("102-Anjali-HR-45000")
e2.display_details()



print("Total Employees:", Employee.total_employees)
