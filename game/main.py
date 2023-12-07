from gears.armor import armor
from gears.weapon import Weapon


little_armor = armor('armure partielle', 50)
mid_armor = armor('armure moyenne', 75)
complete_armor = armor('armure partielle', 100)

sword_weapon = Weapon('Epée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)

armor_choose = input("Quelle armure souhaitez-vous équiper 1, 2, 3 ? (1 : armure partielle, 2 : armure moyenne, 3 : armure complète) : ")
user_armor = ''

if armor_choose == "1":
    user_armor = little_armor
elif armor_choose == "2":
    user_armor = mid_armor
elif armor_choose == "3":
    user_armor = complete_armor
else: 
    print("Vous n'aver pas choisi d'armure")
    

weapon_choose = input("Quelle arme souhaitez-vous équiper 1, 2, 3 ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")
user_weapon = ''

if armor_choose == "1":
    user_weapon = sword_weapon
elif armor_choose == "2":
    user_weapon = pickaxe_weapon
elif armor_choose == "3":
    user_weapon = fist_weapon
else: 
    print("Vous n'aver pas choisi d'armure")
    

if 
print(f"Vous avez une {user_weapon.name} et elle met {user_weapon.damage} de points de dégat")
print(f"Vous avez une {user_armor.name} et elle a {user_armor.defense} de points de défense")
f,jzojiezpfmq