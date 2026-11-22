# 11. Company Hierarchy
# Person
# Employee(Person)
# Manager(Employee)

# Display company hierarchy.

class Person:
    def __init__(self, name):
        self.__name = name      

    
    def get_name(self):
        return self.__name



class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   
        self.__salary = salary  

    
    def get_salary(self):
        return self.__salary



class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.__department = department

    
    def get_department(self):
        return self.__department

    def display(self):
        print("Name:", self.get_name())
        print("Salary:", self.get_salary())
        print("Department:", self.get_department())



m = Manager("Ishika", 50000, "IT")

m.display()