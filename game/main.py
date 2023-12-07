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

def choose_equipment(character_name):
    print(f"Équipement pour {character_name}:")
    
    # Armor selection
    armor_choose = input(f"Quelle armure souhaitez-vous équiper pour {character_name} ? (1 : armure partielle, 2 : armure moyenne, 3 : armure complète) : ")
    if armor_choose == "1":
        user_armor = little_armor
    elif armor_choose == "2":
        user_armor = mid_armor
    elif armor_choose == "3":
        user_armor = complete_armor
    else: 
        print(f"Vous n'avez pas choisi d'armure pour {character_name}")
        return None, None
    
    # Weapon selection
    weapon_choose = input(f"Quelle arme souhaitez-vous équiper pour {character_name} ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")
    if weapon_choose == "1":
        user_weapon = sword_weapon
    elif weapon_choose == "2":
        user_weapon = pickaxe_weapon
    elif weapon_choose == "3":
        user_weapon = fist_weapon
    else: 
        print(f"Vous n'avez pas choisi d'arme pour {character_name}")
        return None, None
    
    return user_armor, user_weapon

# Initialize equipment for Jane
user_armor_jane, user_weapon_jane = choose_equipment("Jane")

# Display equipment for Jane
if user_armor_jane and user_weapon_jane:
    print(f"Jane a une {user_weapon_jane.name} qui met {user_weapon_jane.damage} de points de dégât")
    print(f"Jane a une {user_armor_jane.name} qui a {user_armor_jane.defense} de points de défense")

# Initialize equipment for John
user_armor_john, user_weapon_john = choose_equipment("John")

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
