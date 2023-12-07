from gears.armor import armor
from gears.weapon import Weapon
from characters.character import Character
from characters.barbarian import Barbarian

no_armor = armor("Pas d'armure", 0)
little_armor = armor('armure partielle', 50)
mid_armor = armor('armure moyenne', 75)
complete_armor = armor('armure complète', 100)

sword_weapon = Weapon('Epée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)

# Ask for Jane's equipment
armor_choose_jane = input("Quelle armure souhaitez-vous équiper pour Jane ? (1 : armure partielle, 2 : armure moyenne, 3 : armure complète) : ")
weapon_choose_jane = input("Quelle arme souhaitez-vous équiper pour Jane ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")

# Ask for John's equipment
armor_choose_john = input("Quelle armure souhaitez-vous équiper pour John ? (1 : armure partielle, 2 : armure moyenne, 3 : armure complète) : ")
weapon_choose_john = input("Quelle arme souhaitez-vous équiper pour John ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")

# Initialize equipment for Jane
user_armor_jane = None
user_weapon_jane = None

if armor_choose_jane == "1":
    user_armor_jane = little_armor
elif armor_choose_jane == "2":
    user_armor_jane = mid_armor
elif armor_choose_jane == "3":
    user_armor_jane = complete_armor
else: 
    print("Vous n'avez pas choisi d'armure pour Jane")

if weapon_choose_jane == "1":
    user_weapon_jane = sword_weapon
elif weapon_choose_jane == "2":
    user_weapon_jane = pickaxe_weapon
elif weapon_choose_jane == "3":
    user_weapon_jane = fist_weapon
else: 
    print("Vous n'avez pas choisi d'arme pour Jane")

# Initialize equipment for John
user_armor_john = None
user_weapon_john = None

if armor_choose_john == "1":
    user_armor_john = little_armor
elif armor_choose_john == "2":
    user_armor_john = mid_armor
elif armor_choose_john == "3":
    user_armor_john = complete_armor
else: 
    print("Vous n'avez pas choisi d'armure pour John")

if weapon_choose_john == "1":
    user_weapon_john = sword_weapon
elif weapon_choose_john == "2":
    user_weapon_john = pickaxe_weapon
elif weapon_choose_john == "3":
    user_weapon_john = fist_weapon
else: 
    print("Vous n'avez pas choisi d'arme pour John")

# Display equipment for Jane
if user_armor_jane and user_weapon_jane:
    print(f"Jane a une {user_weapon_jane.name} qui met {user_weapon_jane.damage} de points de dégât")
    print(f"Jane a une {user_armor_jane.name} qui a {user_armor_jane.defense} de points de défense")

# Display equipment for John
if user_armor_john and user_weapon_john:
    print(f"John a une {user_weapon_john.name} qui met {user_weapon_john.damage} de points de dégât")
    print(f"John a une {user_armor_john.name} qui a {user_armor_john.defense} de points de défense")

# Initialize characters with their respective equipment
jane = Character("Jane", user_armor_jane, user_weapon_jane, 120)
john = Character("John", user_armor_john, user_weapon_john, 100)

# Perform an attack
john.attack(jane)

# Display results
print("Results: ")
print(john.name, john.hp, "HP et", john.armor.defense, "de defense")
print(jane.name, jane.hp, "HP et", jane.armor.defense, "de defense")
print("------------------")
