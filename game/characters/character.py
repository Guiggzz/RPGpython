from gears.armor import armor
from gears.weapon import Weapon
from Barbarian import Barbarian

class Character:
    def __init__(self, name, armor: armor, weapon: Weapon = Weapon('Le saint batôn de berger'), hp: float = 100):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp

        self.armor_name = self.armor.name
        self.armor_defense = self.armor.defense
        self.weapon_name = self.weapon.name
        self.weapon_damage = self.weapon.damage

    def get_armor_info(self):
        return f"Armor: {self.armor_name}, Defense: {self.armor_defense}"

    def get_weapon_info(self):
        return f"Weapon: {self.weapon_name}, Damage: {self.weapon_damage}"
    
    def attack(self, other):
        if other.armor.defense >= self.weapon.damage:
            other.armor.defense -= self.weapon.damage
        else:
            other.hp -= self.weapon.damage - other.armor.defense
            other.armor.defense = 0