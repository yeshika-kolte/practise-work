# 12. University System
# Person
# Student(Person)
# GraduateStudent(Student)

# Add thesis information.

class Person:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no


class Student(Person):
    def __init__(self, name, roll_no, thesis_id):
        super().__init__(name, roll_no)
        self.__thesis_id = thesis_id

    def get_thesis_id(self):  
        return self.__thesis_id


class GraduateStudent(Student):
    def __init__(self, name, roll_no, thesis_id, thesis_title):
        super().__init__(name, roll_no, thesis_id)
        self.__thesis_title = thesis_title

    def get_thesis_title(self):
        return self.__thesis_title



p = Person("Rahul", 101)
s = Student("Anjali", 102, "cs101")
g = GraduateStudent("Amit", 103, "ml201", "Deep Learning for NLP")

print(p.get_name(), p.get_roll_no())
print(s.get_name(), s.get_roll_no(), s.get_thesis_id())
print(g.get_name(), g.get_roll_no(), g.get_thesis_id(), g.get_thesis_title())
