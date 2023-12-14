from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapon
from characters.barbarian import Barbarian
from characters.wizard import Wizard
from gears.spell import Spell
import time

class Arena : 
    def __init__(self, first_character:Character, second_character:Character):
        self.first_character = first_character
        self.second_character = second_character

    def fight(self, first_character, second_character):
        print("-------------------------------")
        print("Résultats : ")
        print(self.first_character.name, "a", self.first_character.hp, "PV et",  self.first_character.defense, 'de défense')
        print(self.second_character.name, "a", self.second_character.hp, "PV et",  self.second_character.defense, 'de défense')
        print("-------------------------------")
        while self.first_character.hp > 0 or self.second_character.hp > 0:
            self.first_character.attack(self.second_character)
            print("-------------------------------")
            print("Résultats : ")
            print(self.first_character.name, "a", self.first_character.hp, "PV et",  self.first_character.defense, 'de défense')
            print(self.second_character.name, "a", self.second_character.hp, "PV et",  self.second_character.defense, 'de défense')
            print("-------------------------------")
            time.sleep(3.5)
            self.second_character.attack(self.first_character)
            print("-------------------------------")
            print("Résultats : ")
            print(self.second_character.name, "a", self.second_character.hp, "PV et",  self.second_character.defense, 'de défense')
            print(self.first_character.name, "a", self.first_character.hp, "PV et",  self.first_character.defense, 'de défense')
            print("-------------------------------")
            time.sleep(3.5)




