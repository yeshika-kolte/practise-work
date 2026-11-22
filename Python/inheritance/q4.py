'''4. Student Management

Base class Person.

Derived:

Student
Teacher

Add role-specific methods.
'''
from abc import *
class Person(ABC):
    @abstractmethod
    def role(self):
        pass


class Student(Person):
    def role(self):
        print("I am Student")


class Teacher(Person):
    def role(self):
        print("I am Teacher")



student = Student()
student.role()

teacher = Teacher()
teacher.role()

