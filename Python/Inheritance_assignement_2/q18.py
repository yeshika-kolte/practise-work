from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def grade(self, marks):
        pass

class SchoolStudent(Student):
    def grade(self, marks):
        if marks >= 90:
            print("School Grade : A")
        elif marks >= 75:
            print("School Grade : B")
        else:
            print("School Grade : C")

class CollegeStudent(Student):
    def grade(self, marks):
        if marks >= 85:
            print("College Grade : O")
        elif marks >= 70:
            print("College Grade : A")
        else:
            print("College Grade : B")

obj1 = SchoolStudent()
obj1.grade(92)

obj2 = CollegeStudent()
obj2.grade(78)