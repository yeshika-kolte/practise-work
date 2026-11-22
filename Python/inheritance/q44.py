from abc import ABC, abstractmethod

class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Exam(ABC):
    @abstractmethod
    def conduct_exam(self):
        pass

class OnlineExam(Exam):
    def __init__(self, subject, marks):
        self.__subject = subject
        self.__marks = marks

    def get_subject(self):
        return self.__subject

    def get_marks(self):
        return self.__marks

    def conduct_exam(self):
        print(f"Exam Sub: {self.get_subject()}")

class Result:
    def __init__(self, student, exam):
        self.__student = student
        self.__exam = exam

    def display_result(self):
        print(f"Student : {self.__student.get_name()}")
        print(f"Subject : {self.__exam.get_subject()}")
        print(f"Marks : {self.__exam.get_marks()}")

        if self.__exam.get_marks() >= 30:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Rahul")
e1 = OnlineExam("Python", 75)
e1.conduct_exam()
r1 = Result(s1, e1)
r1.display_result()