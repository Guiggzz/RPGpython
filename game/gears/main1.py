# ... (previous code remains unchanged)

while fight_condition:
    First_character_response = inquirer.prompt(questions_character)
    First_character = First_character_response['choice_character']
    answers = inquirer.prompt(questions_fighter)

    if answers['choice_fighter'] == 'Barbare (Attaque 2 fois)' or answers['choice_fighter'] == 'Sorcier (utilise des sorts)':
        if answers['choice_fighter'] == "Barbare (Attaque 2 fois)":
            # ... (previous code remains unchanged)

            # Ensure that armor and weapon conditions are met
            if armor_condition and weapon_condition:
                print(f'\nVous avez choisi : \n{user_weapon.name} pour attaquer et une {user_armor.name} qui a {user_armor.defense} de défense pour vous protéger')
                print(f"\nVotre {user_weapon.name} inflige : \n{user_weapon.damage} de dégâts et l'{user_armor.name} de votre adversaire a {Second_fighter.armor.defense} de défense")
            else:
                print("Vous n'avez pas choisi d'équipement valide")
        else:
            # ... (previous code remains unchanged)

            # Ensure that armor and weapon conditions are met
            if armor_condition and weapon_condition:
                print(f'\nVous avez : \n un bâton qui inflige 20 de dégâts, un sort {user_spell.name} qui inflige {user_spell.damage} de dégâts, une {user_armor.name} qui a {user_armor.defense} de défense pour vous protéger')
                print(f"\nVotre adversaire a {Second_fighter.hp} de vie et {Second_fighter.armor.defense} de défense")
            else:
                print("Vous n'avez pas choisi d'équipement valide")

        # ... (rest of your code remains unchanged)
