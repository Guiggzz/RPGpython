from gears.armor import Armor
from gears.weapon import Weapon
from random import randint

class Character:
    def __init__(self, name, armor=None, weapon=None, hp=100):
        self.name = name 
        self.armor = armor if armor else Armor('armure partielle')
        self.weapon = weapon if weapon else Weapon('Le saint bâton de berger')
        self.hp = hp
        self.defense = self.armor.defense
    def attack(self, other): 
        random_value = randint(1, 100)
        if random_value >= 5:
            if other.armor is not None:
                if other.armor.defense >= self.weapon.damage:
                    other.armor.defense -= self.weapon.damage
                else:
                    other.hp -= self.weapon.damage - other.armor.defense
                    other.armor.defense = 0
            else:
                other.hp -= self.weapon.damage
            if 90 <= random_value <= 100:
                print("Vous allez mettre un coup critique qui met 2x plus de dégats")
                if other.armor is not None:
                    if other.armor.defense >= self.weapon.damage:
                        other.armor.defense -= self.weapon.damage
                    else:
                        other.hp -= self.weapon.damage - other.armor.defense
                        other.armor.defense = 0
                else:
                    other.hp -= self.weapon.damage
        else:
            print("L'attaque n'est pas parvenue à la cible...")