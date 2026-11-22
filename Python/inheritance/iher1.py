#1. Animal Sound System
#Create parent class Animal and child classes:
#Dog
#Cat
#Cow
#Override sound() method.

class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
class Cow(Animal):
    def sound(self):
        return "Moow"
Dog = Dog()
cat = Cat()
cow = Cow()        

print(Dog.sound())
print(cat.sound())
print(cow.sound())

