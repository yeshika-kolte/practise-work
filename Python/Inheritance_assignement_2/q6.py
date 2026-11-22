'''6. Exam Evaluation System
Problem Statement

Marks are evaluated differently.

Create:

abstract class Exam

Child:

MCQExam
PracticalExam
VivaExam

Each calculates grades differently.'''

from abc import *

class Exam(ABC):

    @abstractmethod
    def grade(self):
        pass

class MCQ(Exam):
    def __init__(self,marks):
        self.__marks = marks

    def grade(self):
        print("MCQ Grade")
        if self.__marks >85 and self.__marks <100:
            print('A Grade')
        elif self.__marks >65  and self.__marks <=85:
            print("B Grade")

        elif self.__marks >33 and self.__marks <=65:
            print("C Grade")

        else:
            print("Fail")

class PracticalExam(Exam):
    def __init__(self,marks):
        self.__marks = marks

    def grade(self):
        print("Practical Exam Grade")
        if self.__marks >85 and self.__marks <100:
            print('A Grade')
        elif self.__marks >65  and self.__marks <=85:
            print("B Grade")

        elif self.__marks >33 and self.__marks <=65:
            print("C Grade")

        else:
            print("Fail")
class Viva(Exam):
    def __init__(self,marks):
        self.__marks = marks

    def grade(self):
        print("Viva Grade")
        if self.__marks >85 and self.__marks <100:
            print('A Grade')
        elif self.__marks >65  and self.__marks <=85:
            print("B Grade")

        elif self.__marks >33 and self.__marks <=65:
            print("C Grade")

        else:
            print("Fail")


mcq = MCQ(89)
mcq.grade()

pe = PracticalExam(76)
pe.grade()

viva = Viva(90)
viva.grade()