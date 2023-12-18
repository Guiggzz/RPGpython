from gears.armor import Armor
from gears.weapon import Weapon
from characters.character import Character

class Barbarian:
    def __init__(self, name, armor: Armor = Armor('Armure legere'), weapon: Weapon = Weapon('Le saint batôn de berger'), hp: float = 100):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp

    def attack(self, other):
        for _ in range(2):
            Character.attack(self, other)
