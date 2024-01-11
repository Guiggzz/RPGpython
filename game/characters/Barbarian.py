from gears.armor import Armor
from gears.weapon import Weapon
from characters.character import Character

class Barbarian(Character):
    def __init__(self, name, armor=None, weapon=None, hp=120):
        super().__init__(name, armor, weapon, hp)

        if weapon is not None:
            self.weapon.damage = weapon.damage
            
    def attack(self, other):
        for _ in range(2):
            Character.attack(self, other)
