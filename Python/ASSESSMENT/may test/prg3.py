# Question 3 — Abstract Class

# Create an abstract class Shape.

# Requirements:

# Use the ABC module.

# Create an abstract method:

# area()

# Create two child classes:

# Rectangle
# Circle

# Implement the area() method in both classes.

# Formula
# Rectangle Area = length × breadth
# Circle Area = π × r × r

# Take input from the user and display the calculated area.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def get_breadth(self):
        return self.__breadth

    def area(self):
        return self.__length * self.__breadth


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        pi = 3.14
        return pi * self.__radius * self.__radius


print("Make a choice to calculate area press 1 for rectangle and 2 for circle")
choice = int(input(" choice: "))

if choice == 1:
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    rect = Rectangle(length, breadth)
    print(f"Area of Rectangle = {rect.area()}")

elif choice == 2:
    radius = int(input("Enter radius: "))
    circ = Circle(radius)
    print(f"Area of Circle = {circ.area()}")

else:
    print("Invalid choice!")
