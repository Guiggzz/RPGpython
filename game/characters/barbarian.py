
from gears.armor import armor
from gears.weapon import Weapon
from characters.character import Character

class Barbarian(Character):
    def __init__(self, name, armor, weapon, hp):
        super().__init__(name, armor, weapon, hp)



    def attack(self, other):
        for _ in range(2):
            Character.attack(self, other)
