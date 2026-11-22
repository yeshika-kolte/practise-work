from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

class Archer(Character):
    def attack(self):
        print("Archer attacks with Bow and Arrow")

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with Sword")

class Mage(Character):
    def attack(self):
        print("Mage attacks with Magic Spell")

obj1 = Archer()
obj1.attack()

obj2 = Warrior()
obj2.attack()

obj3 = Mage()
obj3.attack()