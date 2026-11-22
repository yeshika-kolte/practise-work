# PART 3 — Abstract Class Exercises
# 21. Shape Area Calculator

# Abstract class Shape.

# Derived:

# Circle
# Rectangle
# Triangle

# Implement area calculation.

from abc import *

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def get_area(self):
        self.r = float(input("Enter Radius"))
        print(f"Area of Circle : {3.14 * self.r * self.r}")
    

class Triangle(Shape):
    def get_area(self):
        self.b = int(input("Enter Base"))
        self.h = int(input("Enter Height"))
        print(f"Area of Triangle : {1/2 * self.b * self.h }")
       
    
class Rectangle(Shape):
    def get_area(self):
        self.l = int(input("Enter Length"))
        self.w = int(input("Enter Width"))
        print(f"Area of Rectangle : {self.l * self.w}")


obj = None

print("Choose 1 for Area of Circle")
print("Choose 2 for Area of Triangle")
print("Choose 3 for Area of Rectangle")

choice = int(input("Enter choice"))

if choice == 1:
    obj = Circle()

elif choice == 2:
    obj = Triangle()

elif choice == 3:
    obj = Rectangle()


obj.get_area()
