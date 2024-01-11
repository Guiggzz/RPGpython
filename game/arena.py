from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapon
from characters.barbarian import Barbarian
from characters.wizard import Wizard
from gears.spell import Spell
import time

class Arena:
    def __init__(self, first_character, second_character):
        self.first_character = first_character
        self.second_character = second_character

    def fight(self):
        self.print_mini_bilan() 
        input("\nEntrez pour commencer le combat")
        while self.first_character.hp > 0 and self.second_character.hp > 0:
            self.first_character.attack(self.second_character)
            print("\nPerso 1 attaque")
            self.print_mini_bilan()    
            input("\nEntrez pour passer au tour suivant")      
            if self.second_character.hp <= 0:
                break  
            self.second_character.attack(self.first_character)
            print("\nPerso 2 attaque")
            self.print_mini_bilan()
            input("\nEntrez pour passer au tour suivant")


        self.print_final_bilan()

    def print_mini_bilan(self):
        if self.first_character.hp >= 0 and self.second_character.hp >= 0:
            print("Mini-Bilan :\n")
            print(f"{self.first_character.name} a {self.first_character.hp} HP restants et {self.first_character.armor.defense} d'armure.")
            print(f"{self.second_character.name} a {self.second_character.hp} HP restants et {self.second_character.armor.defense} d'armure.")
            print("-----------------------------")
        elif self.first_character.hp <=0 :
            print("Mini-Bilan :\n")
            print(f"{self.first_character.name} a 0 HP restants.")
            print(f"{self.second_character.name} a {self.second_character.hp} HP restants et {self.second_character.armor} d'armure.")
            print("-----------------------------")
        elif self.second_character.hp <=0 :
            print("Mini-Bilan :\n")
            print(f"{self.first_character.name} a {self.first_character.hp} HP restants et {self.first_character.armor} d'armure.")
            print(f"{self.second_character.name} a 0 HP restants.")
            print("-----------------------------")   


    def print_final_bilan(self):
        print("\nBilan final :")
        if self.first_character.hp <= 0:
            print(f"{self.first_character.name} est vaincu !")
        elif self.second_character.hp <= 0:
            print(f"{self.second_character.name} est vaincu !")
        print("-----------------------------")