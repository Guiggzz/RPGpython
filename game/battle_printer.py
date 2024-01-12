from characters.barbarian import Barbarian
from characters.wizard import Wizard
from characters.character import Character
# from characters.bestiaire import Monster
class BattlePrinter:
    def print_bilan(self, first_character, first_fighter, second_character, second_fighter):
        print("-------------------------------")
        print("Bilan: ")
        print(f"{first_character} à {first_fighter.hp} HP")
        print(f"{second_character} à {second_fighter.hp} HP et {second_fighter.armor.defense} de defense")
        if isinstance(first_fighter, Wizard): 
            first_fighter.print_mana()
        print("-------------------------------")

    def print_bilan_final(self, first_character, first_fighter, second_character, second_fighter):
        print("--------------------------------")
        print("Résultats finaux : ")
        print(f"{first_character} à {first_fighter.hp} HP")
        print(f"{second_character} à 0 HP et 0 de defense")
        if isinstance(first_fighter, Wizard): 
            first_fighter.print_mana()
        print("--------------------------------")

    def print_mini_bilan(self, first_fighter, second_fighter):
        if isinstance(first_fighter, Character) and isinstance(second_fighter, Character):
            if first_fighter.hp >= 0 and second_fighter.hp >= 0:
                print(f"\n{first_fighter.name} a {first_fighter.hp} HP")
                print(f"{second_fighter.name} a {second_fighter.hp} HP")
            else:
                print("\nLe combat est terminé !")
                print(f"{first_fighter.name} a {first_fighter.hp} HP")
                print(f"{second_fighter.name} a {second_fighter.hp} HP")
        else:
            print("\nLe combat est terminé !")
            print(f"{first_fighter.name} a {first_fighter.hp} HP")
            print(f"{second_fighter.name} a {second_fighter.hp} HP")
            
    def print_mini_final_bilan(self, first_character, first_fighter, second_character, second_fighter):
        print("\nBilan final :")
        if first_fighter.hp <= 0:
            print(f"{first_character.name} est vaincu !")
        elif second_fighter.hp <= 0:
            print(f"{second_character.name} est vaincu !")
        print("-----------------------------")

    def print_mini_bilan_monstre(self, first_fighter, second_fighter):
        if isinstance(first_fighter, Character) and isinstance(second_fighter, Character):
            if first_fighter.hp >= 0 and second_fighter.hp >= 0:
                print(f"\n{first_fighter.name} a {first_fighter.hp} HP")
                print(f"{second_fighter.name} a {second_fighter.hp} HP")
            else:
                print("\nLe combat est terminé !")
                print(f"{first_fighter.name} a {first_fighter.hp} HP")
                print(f"{second_fighter.name} a {second_fighter.hp} HP")
        else:
            print("\nLe combat est terminé !")
            print(f"{first_fighter.name} a {first_fighter.hp} HP")
            print(f"{second_fighter.name} a {second_fighter.hp} HP")

    def print_mini_final_bilan_monstre(self, first_character, first_fighter, second_character, second_fighter):
        print("\nBilan final :")
        if first_fighter.hp <= 0:
            print(f"{first_fighter.name} est vaincu !")
        elif second_fighter.hp <= 0:
            print(f"{second_fighter.name} est vaincu !")
        print("-----------------------------")
from arena import Arena
