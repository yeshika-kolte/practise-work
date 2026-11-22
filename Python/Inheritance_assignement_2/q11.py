'''11. Shape Drawing Application
Problem Statement

A drawing app supports multiple shapes.

Create abstract class Shape.

Child:

Circle
Rectangle
Triangle

Each implements:

draw()
area()'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Drawing Circle")

    def area(self):
        a = math.pi * self.radius * self.radius
        print(f"Circle Area: {a}")


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def draw(self):
        print("Drawing Rectangle")

    def area(self):
        a = self.length * self.breadth
        print(f"Rectangle Area: {a}")


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        print("Drawing Triangle")

    def area(self):
        a = 0.5 * self.base * self.height
        print(f"Triangle Area: {a}")


c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

c.draw()
c.area()

r.draw()
r.area()

t.draw()
t.area()