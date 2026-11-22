# Question 2 — Multilevel Inheritance

# Create the following class hierarchy:

# Person → Teacher → PythonTrainer

# Requirements:

# Person
# variable: name
# method: show_person()
# Teacher
# variable: subject
# method: show_teacher()
# PythonTrainer
# variable: experience
# method: show_trainer()

# Create an object of PythonTrainer and display all details using inherited methods.

class Person:
    def __init__(self,name):
        self.name =name
    def show_person(self):
        print(f"Name:{self.name}")

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def show_teacher(self):
        print(f"Subject:{self.subject}")

class PythonTrainer(Teacher):
    def __init__(self,name,subject,experience):
        super().__init__(name,subject)
        self.experience=experience
    def show_trainer(self):
        print(f"Experience: {self.experience}")    

object= PythonTrainer("yeshika" ,"machine_learning", 9)
object.show_person()
object.show_teacher()
object.show_trainer()     