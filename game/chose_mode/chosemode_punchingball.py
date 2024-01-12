from battle_printer import BattlePrinter
from characters.Barbarian import Barbarian
from characters.wizard import Wizard
import inquirer
from game_questions import GameQuestions
from player_selection import PlayerSelections
from chose_mode.chosemode_arena import arena_mode

class ModeSelections:
    pass  # Laissez cette classe vide pour éviter l'importation circulaire

# Initialisation de fight_condition
ModeSelections.fight_condition = False

def punchingBall_mode(game_questions, player_selections, answers, fist_weapon, sword_weapon):
    mode_selection_instance = ModeSelections()  # Créez une instance de la classe ModeSelections
    mode_selection_instance.fight_condition = True  # Initialisez fight_condition
    while mode_selection_instance.fight_condition:
                First_character_response = inquirer.prompt(game_questions.questions_character)
                First_character = First_character_response['choice_character']
                answers = inquirer.prompt(game_questions.questions_fighter)
                if answers['choice_fighter'] == 'Barbare (Attaque 2 fois)' or answers['choice_fighter'] == 'Sorcier (utilise des sorts)':
                    if answers['choice_fighter'] == "Barbare (Attaque 2 fois)":
                        answers = inquirer.prompt(game_questions.questions_weapon)
                        user_weapon = None
                        weapon_condition = True
                        First_character_armor = None
                        player_selections.select_weapon(answers)
                        First_fighter = Barbarian(First_character, First_character_armor, user_weapon, 120)
                    else:
                        answers = inquirer.prompt(game_questions.questions_spell)
                        user_spell = None
                        weapon_condition = True
                        First_character_armor = None
                        player_selections.select_spell(answers)
                        First_fighter = Wizard(First_character, First_character_armor, user_spell, 75, fist_weapon, 60)
                Second_character_response = inquirer.prompt(game_questions.questions_character)
                Second_character = Second_character_response['choice_character']
                answers = inquirer.prompt(game_questions.questions_fighter)
                attack_type = True
                if answers['choice_fighter'] == 'Barbare (Attaque 2 fois)' or answers['choice_fighter'] == 'Sorcier (utilise des sorts)':
                    if answers['choice_fighter'] == "Barbare (Attaque 2 fois)":
                        answers = inquirer.prompt(game_questions.questions_weapon)
                        user_weapon = None
                        weapon_condition = True
                        player_selections.select_weapon(answers)
                        answers = inquirer.prompt(game_questions.questions_armor)
                        user_armor = None
                        armor_condition = True
                        player_selections.select_armor(answers)
                        Second_fighter = Barbarian(Second_character, user_armor, user_weapon, 120)
                    else:
                        answers = inquirer.prompt(game_questions.questions_spell)
                        user_spell = None
                        weapon_condition = True
                        player_selections.select_spell(answers)
                        answers = inquirer.prompt(game_questions.questions_armor)
                        user_armor = None
                        armor_condition = True
                        player_selections.select_armor(answers)
                        player = Wizard(player_character, None, player_selections.user_spell, 75, fist_weapon, 60)
                    if isinstance(First_fighter, Barbarian):
                        if armor_condition and weapon_condition:
                                print(f'\nVous avez choisi : \n{First_fighter.weapon.name} pour attaquer')
                                print(f"\nVotre {First_fighter.weapon.name} inflige : \n{First_fighter.weapon.damage} de dégâts et l'{Second_fighter.armor.name} de votre adversaire a {Second_fighter.armor.defense} de défense.")
                        else:
                           print("Vous n'avez pas choisi d'équipement valide")
                    else:
                            if isinstance(First_fighter, Wizard): 
                                print(f'\nVous avez : \n un bâton qui inflige 20 de dégâts, un sort {First_fighter.spell.name} qui inflige {First_fighter.spell.damage} de dégâts.')
                                print(f"\nVotre adversaire a {Second_fighter.hp} de vie et {Second_fighter.armor.defense} de défense")
                            else:
                                print("Vous n'avez pas choisi d'équipement valide")
                    if isinstance(First_fighter, Barbarian): 
                        print("\nVous avez la classe Barbare. Vous attaquez deux fois d'affilée !")
                    elif isinstance(First_fighter, Wizard):
                        print("\nVous avez la classe Sorcier. Vous avez des sorts.") 
                        battle_printer = BattlePrinter()
                        battle_printer.print_bilan(First_character, First_fighter, Second_character, Second_fighter)
                    attack_type = True
                    while attack_type == True:
                        answers = inquirer.prompt(game_questions.questions_fight)
                        if answers['choice_fight'] == 'Oui':
                            First_fighter.attack(Second_fighter)
                            if Second_fighter.hp > 0:
                                battle_printer = BattlePrinter()
                                battle_printer.print_bilan(First_character, First_fighter, Second_character, Second_fighter)
                            else : 
                                print("Vous avez vaincu votre adversaire (il est mort)")
                                battle_printer = BattlePrinter()
                                battle_printer.print_bilan_final(First_character, First_fighter, Second_character, Second_fighter)
                                attack_type = False
                                mode_selection_instance.fight_condition = False
                        elif answers['choice_fight'] == 'Non':
                            battle_printer = BattlePrinter()
                            battle_printer.print_bilan_final(First_character, First_fighter, Second_character, Second_fighter)
                            attack_type = False
                            mode_selection_instance.fight_condition = False
                        else :
                                print("Vous n'avez pas choisi d'action valide")
                                attack_type = False
                                mode_selection_instance.fight_condition = False
                else:
                    print("Au revoir !")
                    break