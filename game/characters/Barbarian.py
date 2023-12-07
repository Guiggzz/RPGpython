from gears.armor import armor
from gears.weapon import Weapon
from characters.character import Character

class Barbarian:
    def __init__(self, name, armor: armor, weapon: Weapon = Weapon('Le saint batôn de berger'), hp: float = 80, character_type = None):
        self.name = name
        self.hp = hp
        self.character_type = character_type
        
    def attack(self, other):
        for _ in range(2):
            Character.attack(self, other)