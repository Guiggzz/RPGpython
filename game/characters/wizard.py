# from characters.character import Character
from gears.spell import Spell
from gears.armor import Armor
from gears.weapon import Weapon
from characters.character import Character
class Wizard:
    def __init__(self, name, armor, spell:Spell, hp=75, weapon='Saint Batons de berger', damage:float = 20, mana:float=100):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.damage = damage
        self.hp = hp
        self.spell = spell
        self.mana = mana 
    def attack(self, other):
        answer_user = input("'Y' pour lancer un sort, 'N' pour attaquer avec votre baton\n")
        if answer_user == 'Y':
            if self.mana >= self.spell.mana:
                if other.armor is not None:
                    if other.armor.defense >= self.spell.damage:
                        other.armor.defense -= self.spell.damage
                        self.mana -= self.spell.mana
                    else:
                        other.hp -= self.spell.damage - other.armor.defense
                        other.armor.defense = 0
                        self.mana -= self.spell.mana
                else:
                    other.hp -= self.spell.damage
            else : 
                self.mana += 15
                if other.armor is not None:
                    if other.armor.defense >= self.weapon.damage:
                        other.armor.defense -= self.weapon.damage
                        print('Pas asser de mana, vous attaquer donc avec vos coup de poing')
                    else:
                        other.hp -= self.weapon.damage - other.armor.defense
                        other.armor.defense = 0
                        print('Pas asser de mana, vous attaquer donc avec vos coup de poing')
                else:
                    print("test")
                    other.hp -= self.weapon.damage
        else:
            Character.attack(self, other)

    def print_mana(self):
        print(f'Vous avez {self.mana} mana')