from characters.character import Character
from gears.armor import armor
from gears.weapon import Weapon
from characters.barbarian import Barbarian
from characters.wizard import Wizard

little_armor = armor('armure partielle', 50)
mid_armor = armor('armure moyenne', 75)
complete_armor = armor('armure complète', 100)

sword_weapon = Weapon('Epée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)

weapon_choose = input("\nQuelle arme souhaitez-vous équiper 1, 2, 3 ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")
user_weapon = None

if weapon_choose == "1":
    user_weapon = sword_weapon
    weapon_condition = True
elif weapon_choose == "2":
    user_weapon = pickaxe_weapon
    weapon_condition = True
elif weapon_choose == "3":
    user_weapon = fist_weapon
    weapon_condition = True
else:
    weapon_condition = False


armor_choose = input("\nQuelle armure souhaitez-vous équiper 1, 2, 3 ? (1 : Petite armure, 2 : Moyenne armure, 3 : Grosse armure) : ")
user_armor = None

if armor_choose == "1":
    user_armor = little_armor
    armor_condition = True
elif armor_choose == "2":
    user_armor = mid_armor
    armor_condition = True
elif armor_choose == "3":
    user_armor = complete_armor
    armor_condition = True
else: 
    armor_condition = False

type_choose = input("Choississez le type de votre personnage 1 : Barbarre ou 2 : Sorcier")

if type_choose == "1":
     jane = Barbarian("Jane", user_armor, user_weapon, 120, user_armor.defense)
else:
     jane = Wizard("Jane", user_armor, user_weapon, 120, user_armor.defense)

john = Character("John", mid_armor, pickaxe_weapon, 100, mid_armor.defense)
attack_type = True

if armor_condition and weapon_condition:
        print(f'\nVous avez choisi : \n{user_weapon.name} pour attaquer et une {user_armor.name} qui à {user_armor.defense} de défense pour vous protéger')
        print(f"\nVotre {user_weapon.name} met : \n{user_weapon.damage} de degat et l'{user_armor.name} de votre advairsaire à {john.defense} de defense")

else:
        print("Vous n'avez pas choisi d'équipement valide")
if isinstance(jane, Barbarian): 
    print("\nVous avez la classe Barbare. Vous tapez deux fois d'affilée!")
attack_type = True
while attack_type == True:
    attack_value = input(f"\nVoulez vous attaquer votre enemie ? 1 : Oui, 2 : Non : ")
    if attack_value == "1":
        jane.attack(john)
        if john.hp > 0:
            print("-------------------------------")
            print("Results: ")
            print(john.name, "à", john.hp, "HP et",  john.armor.defense, 'de defense')
            print(jane.name, 'à', jane.hp, "HP et", jane.armor.defense, 'de defense')
            print("-------------------------------")
        else : 
         print("Vous avez terrasser votre advairsaire (il est mort)")
         attack_type = False
    elif attack_value == "2":
        print("--------------------------------")
        print("Results final : ")
        print(john.name, "à", john.hp, "HP et",  john.armor.defense, 'de defense')
        print(jane.name, 'à', jane.hp, "HP et", jane.armor.defense, 'de defense')
        print("--------------------------------")
        attack_type = False
    else :
            print("Vous n'avez pas choisi d'action valide")

        

