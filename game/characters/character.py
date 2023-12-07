from gears.armor import armor
from gears.weapon import Weapon

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
        if self.weapon_name == 'Epée':
            if other.armor_defense >= 30:
                other.armor_defense -= 30
                print(f'{self.name} attaque {other.name} avec une {self.weapon_name}')
            else:
                other.hp -= 30
                print(f'{self.name} attaque {other.name} avec une {self.weapon_name}')
        elif self.weapon_name == 'Pioche':
            if other.armor_defense >= 25:
                other.armor_defense -= 25
                print(f'{self.name} attaque {other.name} avec une {self.weapon_name}')
            else:
                other.hp -= 25
                print(f'{self.name} attaque {other.name} avec une {self.weapon_name}')
        elif self.weapon_name == 'Coup de poing':
            if other.armor_defense >= 20:
                other.armor_defense -= 20
                print(f'{self.name} attaque {other.name} avec ses {self.weapon_name}')
            else:
                other.hp -= 20
                print(f'{self.name} attaque {other.name} avec ses{self.weapon_name}')

