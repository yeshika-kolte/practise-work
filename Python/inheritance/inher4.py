# 4. Student Management

# Base class Person.

# Derived:

# Student
# Teacher

# Add role-specific methods.

class Person:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role       

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role


class Student(Person):
    def __init__(self, name):
        super().__init__(name, "Student")

    def get_role(self):
        return f"{self.get_name()} is a {super().get_role()}"


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name, "Teacher")

    def get_role(self):
        return f"{self.get_name()} is a {super().get_role()}"


student = Student("Ganesh")
teacher = Teacher("Siaaa")

print(student.get_role())
print(teacher.get_role())
  