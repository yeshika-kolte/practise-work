class student :
    total_students = 0
    def __init__(self,roll_no,name,mark_1,mark_2,mark_3):
        self.roll_no = roll_no
        self.name = name
        self.mark_1 = mark_1
        self.mark_2 = mark_2
        self.mark_3 = mark_3
        student.total_students += 1
    def total_marks(self):
        return self.mark_1 + self.mark_2 + self.mark_3
    def calculate_percentage(self):
        total = self.total_marks()
        percentage = (total / 300) * 100
        return percentage
    def display_details(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, "
              f"Mark 1: {self.mark_1}, Mark 2: {self.mark_2}, Mark 3: {self.mark_3}")
        print(f"Total Marks: {self.total_marks()}, Percentage: {self.calculate_percentage()}%")
s1 = student(1,"ishika",99,90,98)
s1.display_details()
print("Total Students:", student.total_students)
