class Student:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

class Attendance:
    def __init__(self, student, status):
        self.__student = student
        self.__status = status

    def display_attendance(self):
        print(f"Student : {self.__student.get_name()}")
        print(f"Attendance : {self.__status}")

class Exam:
    def __init__(self, subject, marks):
        self.__subject = subject
        self.__marks = marks

    def display_exam(self):
        print(f"Subject : {self.__subject}")
        print(f"Marks : {self.__marks}")

class Teacher:
    def __init__(self, teacher_name):
        self.__teacher_name = teacher_name

    def display_teacher(self):
        print(f"Teacher : {self.__teacher_name}")

obj1 = Student("madhur", 101)
obj2 = Attendance(obj1, "Present")
obj2.display_attendance()
obj3 = Exam("Python", 85)
obj3.display_exam()
obj4 = Teacher("pawan Sir")
obj4.display_teacher()