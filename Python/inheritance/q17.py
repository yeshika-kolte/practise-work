'''17. Online Course Platform
Course
ProgrammingCourse
PythonCourse

Add certification system.
'''

class Course:
    def __init__(self, course_name, course_price, course_duration):
        self.__course_name = course_name
        self.__course_price = course_price
        self.__course_duration = course_duration

    def get_course_name(self):
        return self.__course_name

    def get_course_price(self):
        return self.__course_price

    def get_course_duration(self):
        return self.__course_duration


class ProgrammingCourse(Course):
    def __init__(self, name, price, duration, prog_language):
        super().__init__(name, price, duration)
        self.__program_language = prog_language

    def get_progrLang(self):
        return self.__program_language


class PythonCourse(ProgrammingCourse):
    def __init__(self, name, price, duration, lang, instructor, user_name):
        super().__init__(name, price, duration, lang)
        self.__instructor = instructor
        self.__username = user_name

    def course_detail(self):
        print("--------- Course Detail -----------")
        print(f"Course Name : {self.get_course_name()}")
        print(f"Course Price : {self.get_course_price()}")
        print(f"Course Duration : {self.get_course_duration()}")
        print(f"Programming Language : {self.get_progrLang()}")
        print(f"Instructor : {self.__instructor}")

    def certification(self):
        print("--------------- Certification -------------------")
        print(
            f"This is to certify that {self.__username} has successfully "
            f"completed the {self.get_course_duration()} certification course "
            f"in {self.get_course_name()}."
        )


python = PythonCourse(
    "Python Programming",
    10000,
    "3-month",
    "English",
    "Pawan Sir",
    "Anil"
)

python.course_detail()
python.certification()