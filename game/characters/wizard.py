from characters.character import Character
from gears.spell import Spell
from gears.armor import Armor
from gears.weapon import Weapon

class Wizard(Character):
    def __init__(self, name, armor, spell: Spell, hp=75, initial_weapon='Saint Batons de berger', damage: float=20, mana: float=100):
        super().__init__(name, armor, Weapon(initial_weapon, damage), hp)
        self.spell = spell
        self.mana = mana

    def attack(self, other):
        answer_user = input("'Y' pour lancer un sort, 'N' pour attaquer avec votre baton\n")
        if answer_user == 'Y':
            if self.spell and self.mana >= self.spell.mana:
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
            else:
                self.mana += 15
                if other.armor is not None:
                    if other.armor.defense >= self.weapon.damage:
                        other.armor.defense -= self.weapon.damage
                        print('Pas assez de mana, vous attaquez donc avec vos coups de poing')
                    else:
                        other.hp -= self.weapon.damage - other.armor.defense
                        other.armor.defense = 0
                        print('Pas assez de mana, vous attaquez donc avec vos coups de poing')
                else:
                    print("test")
                    other.hp -= self.weapon.damage
        else:
            Character.attack(self, other)

    def print_mana(self):
        print(f'Vous avez {self.mana} mana')
