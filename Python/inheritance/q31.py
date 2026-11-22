from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Drawable):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Drawable):
    def draw(self):
        print("Drawing Rectangle")


class Line(Drawable):
    def draw(self):
        print("Drawing Line")


obj1 = Circle()
obj1.draw()
obj2 = Rectangle()
obj2.draw()
obj3 = Line()
obj3.draw()