from gears.armor import armor
from gears.weapon import Weapon
from characters.character import Character

class Wizard : 
    def __init__(self, name, armor: armor = armor('Armure legere'), hp: float = 75, defense: float = 25, weapon: Weapon = Weapon('Le saint batôn de berger'), damage = 20):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp
        self.defense = defense
        self.damage = damage

    def attack(self, other):
        Character.attack(self, other)

class spell:
    def __init__(self,name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana = mana_cost
    