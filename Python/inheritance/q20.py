'''
20. Gaming Characters
Character
Warrior
SuperWarrior

Add special powers.'''

'''
20. Gaming Characters
Character
Warrior
SuperWarrior

Add special powers.
'''

class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health


class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon


class SuperWarrior(Warrior):
    def __init__(self, name, health, weapon, special_power):
        super().__init__(name, health, weapon)
        self.__special_power = special_power

    def display_character(self):
        print("------ Character Details ------")
        print(f"Name : {self.get_name()}")
        print(f"Health : {self.get_health()}")
        print(f"Weapon : {self.get_weapon()}")
        print(f"Special Power : {self.__special_power}")

    def use_power(self):
        print(f"{self.get_name()} used special power: {self.__special_power}!")


player1 = SuperWarrior(
    "Thor",
    100,
    "Hammer",
    "Thunder Attack"
)

player1.display_character()
player1.use_power()