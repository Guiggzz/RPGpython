from gears.armor import Armor
from gears.weapon import Weapon

class Character:
    def __init__(self, name, armor=None, weapon=None, hp=100):
        self.name = name
        self.armor = armor if armor else Armor('armure partielle')
        self.weapon = weapon if weapon else Weapon('Le saint batôn de berger')
        self.hp = hp
        self.defense = self.armor.defense

    def attack(self, other):
        if other.armor is not None:
            if other.armor.defense >= self.weapon.damage:
                other.armor.defense -= self.weapon.damage
            else:
                other.hp -= self.weapon.damage - other.armor.defense
                other.armor.defense = 0
        else:
            other.hp -= self.weapon.damage
