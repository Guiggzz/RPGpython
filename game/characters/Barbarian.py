from gears.armor import armor
from gears.weapon import Weapon

class Barbarian:
    def __init__(self, name, armor: armor = armor('Armure legere'), weapon: Weapon = Weapon('Le saint batôn de berger'), hp: float = 100, defense: float = 25):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp
        self.defense = defense

    def attack(self, other):
        for _ in range(2):
            if other.armor.defense >= self.weapon.damage:
                other.armor.defense -= self.weapon.damage
            else:
                other.hp -= self.weapon.damage - other.armor.defense
                other.armor.defense = 0
