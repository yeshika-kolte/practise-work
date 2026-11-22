'''
PART 2 — Multilevel & Multiple Inheritance
11. Company Hierarchy
Person
Employee(Person)
Manager(Employee)

Display company hierarchy.'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.__department = department

    def display(self):
        print("----- Company Hierarchy -----")
        print(f"Name       : {self.get_name()}")
        print(f"Age        : {self.get_age()}")
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Salary     : {self.get_salary()}")
        print(f"Department : {self.__department}")


manager1 = Manager("Rahul", 30, 101, 72000, "IT")
manager1.display()