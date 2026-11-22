'''1. Animal Sound System

Create parent class Animal and child classes:

Dog
Cat
Cow

Override sound() method.'''
from abc import *

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog Bark")

class Cat(Animal):
    def sound(self):
        print("Cat Meoww")
   

class Cow(Animal):
    def sound(self):
        print("Cow Mowww")


dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()


