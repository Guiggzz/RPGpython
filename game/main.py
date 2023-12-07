from gears.armor import armor
from gears.weapon import Weapon
from characters.character import Character

#implémentation des armes et armures
no_armor = armor("Pas d'armure", 0)
little_armor = armor('armure partielle', 50)
mid_armor = armor('armure moyenne', 75)
complete_armor = armor('armure complète', 100)

sword_weapon = Weapon('Epée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)


#Demande à l'utilisateurs ce qu'il veut comme équipement
armor_choose = input("Quelle armure souhaitez-vous équiper 1, 2, 3 ? (1 : armure partielle, 2 : armure moyenne, 3 : armure complète) : ")
user_armor = None
equipment_condition = False

weapon_choose = input("Quelle arme souhaitez-vous équiper 1, 2, 3 ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")
user_weapon = None

#choix des armes
if armor_choose == "1":
    user_armor = little_armor
    equipment_condition = True
elif armor_choose == "2":
    user_armor = mid_armor
    equipment_condition = True
elif armor_choose == "3":
    user_armor = complete_armor
    equipment_condition = True
else: 
    print("Vous n'avez pas choisi d'armure")

if weapon_choose == "1":
    user_weapon = sword_weapon
    equipment_condition = True
elif weapon_choose == "2":
    user_weapon = pickaxe_weapon
    equipment_condition = True
elif weapon_choose == "3":
    user_weapon = fist_weapon
    equipment_condition = True
else: 
    print("Vous n'avez pas choisi d'arme")



#print des équipements
if equipment_condition:
    print(f"Vous avez une {user_weapon.name} et elle met {user_weapon.damage} de points de dégât")
    print(f"Vous avez une {user_armor.name} et elle a {user_armor.defense} de points de défense")



#test
jane = Character("Jane", user_armor, user_weapon, 120)
john = Character("John", user_armor, user_weapon, 100)
Barbare = Character("Barbare", user_armor, user_weapon, 100)

Barbare.attack(jane)

print("Results: ")
print(john.name, john.hp, "HP et", john.armor_defense, "de defense")
print(jane.name, jane.hp, "HP et", jane.armor_defense,"de defense")
print(Barbare.name, Barbare.hp, "HP et", Barbare.armor_defense,"de defense")
print("------------------")
