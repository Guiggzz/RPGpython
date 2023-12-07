from gears.armor import armor
from gears.weapon import Weapon

class Character:
    def __init__(self, name, armor: armor, weapon: Weapon = Weapon('Le saint bâton de berger'), hp: float = 100):

        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp

    def get_armor_info(self):
        return f"Armor: {self.armor.name}, Defense: {self.armor.defense}"

    def get_weapon_info(self):
        return f"Weapon: {self.weapon.name}, Damage: {self.weapon.damage}"

    def attack(self, other):
        if other.armor.defense >= self.weapon.damage:
            other.armor.defense -= self.weapon.damage
        else:
            other.hp -= self.weapon.damage - other.armor.defense
            other.armor.defense = 0
