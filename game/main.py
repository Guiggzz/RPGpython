from gears.armor import armor


little_armor = armor('armure partielle', 50)
mid_armor = armor('armure moyenne', 75)
complete_armor = armor('armure partielle', 100)

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


print(f"Vous avez une {user_armor.name} et elle a {user_armor.defense} de points de défense")