from gears.armor import Armor
from gears.weapon import Weapon

class Character:
    def __init__(self, name, armor: Armor = Armor('Armure legere'), weapon: Weapon = Weapon('Le saint batôn de berger'), hp: float = 100, defense: float = 50):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp
        self.defense = defense

    def attack(self, other):
        if other.armor.defense >= self.weapon.damage:
            other.armor.defense -= self.weapon.damage
        else:
            other.hp -= self.weapon.damage - other.armor.defense
            other.armor.defense = 0