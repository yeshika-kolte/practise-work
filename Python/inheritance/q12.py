'''12. University System
Person
Student(Person)
GraduateStudent(Student)

Add thesis information.
'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Student(Person):
    def __init__(self, name, age,roll_no,branch):
        super().__init__(name, age)
        self.__roll_no = roll_no
        self.__branch = branch

    def get_rollno(self):
        return self.__roll_no
    
    def get_branch(self):
        return self.__branch

class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, branch,report):
        super().__init__(name, age, roll_no, branch)
        self.__report = report

    def display(self):
        print("-------------Thesis Information---------------")
        print(f"Student Name : {self.get_name()}")
        print(f"Student Age : {self.get_age()}")
        print(f"Enrollment No. : {self.get_rollno()}")
        print(f"Branch : {self.get_branch()}")
        print(f"Report : {self.__report}")


gs = GraduateStudent("Atul",23,802212,"IT","A thesis report is a structured, written document detailing original research, findings, and analysis, typically required for Bachelor, Master, or PhD degrees. It usually includes an abstract, introduction, literature review, methodology, results, discussion, and conclusion, following a logical flow to support academic candidacy.")
gs.display()