# Import des modules

from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapon
from characters.barbarian import Barbarian
from characters.wizard import Wizard
from gears.spell import Spell
from arena import Arena
import inquirer
from game_questions import GameQuestions
from player_selection import PlayerSelections
from characters.bestiaire import Zombie, Goblin, Dragon, Ghost, Boss, Character, Map
import random

fireball_spell = Spell('Boule de feu', 50, 60)
lightning_spell = Spell('Tonerre', 45, 50)
windwall_spell = Spell("Mur d'air", 30, 30)

little_armor = Armor('armure partielle', 50)
mid_armor = Armor('armure moyenne', 75)
complete_armor = Armor('armure complète', 100)

sword_weapon = Weapon('Épée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)

goblin = Goblin('goblin', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))
dragon = Dragon('dragon', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))
zombie = Zombie('goblin', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))
ghost = Ghost('goblin', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))

game_questions = GameQuestions()
player_selections = PlayerSelections()

sword_weapon = Weapon('Épée', 30)

armor_condition = False
weapon_condition = False
fight_condition = True

class ModeSelections:
    def __init__(self):
        self.user_weapon = None
        self.user_armor = None
        self.user_spell = None
        self.weapon_condition = True
        self.armor_condition = True

    def select_mode(self, choice):
        answers = inquirer.prompt(game_questions.questions_mode)
        if answers['choice_mode'] == 'Punching-Ball (vous etes le seul a attaquer)':
            while fight_condition == True:
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
                        print("-------------------------------")
                        print("Bilan: ")
                        print(First_character, 'à', First_fighter.hp, "HP")
                        print(Second_character, "à", Second_fighter.hp, "HP et",  Second_fighter.armor.defense, 'de defense')
                        if isinstance(First_fighter, Wizard): 
                            First_fighter.print_mana()
                        print("-------------------------------")
                        attack_type = True
                        while attack_type == True:
                            answers = inquirer.prompt(game_questions.questions_fight)
                            if answers['choice_fight'] == 'Oui':
                                First_fighter.attack(Second_fighter)
                                if Second_fighter.hp > 0:
                                    print("-------------------------------")
                                    print("Bilan: ")
                                    print(First_character, 'à', First_fighter.hp, "HP")
                                    print(Second_character, "à", Second_fighter.hp, "HP et",  Second_fighter.armor.defense, 'de defense')
                                    if isinstance(First_fighter, Wizard): 
                                        First_fighter.print_mana()
                                    print("-------------------------------")
                                else : 
                                    print("Vous avez vaincu votre adversaire (il est mort)")
                                    attack_type = False
                                    fight_condition = False
                            elif answers['choice_fight'] == 'Non':
                                print("--------------------------------")
                                print("Résultats finaux : ")
                                print(First_character, 'à', First_fighter.hp, "HP")
                                print(Second_character, "à", Second_fighter.hp, "HP et",  Second_fighter.armor.defense, 'de defense')
                                if isinstance(First_fighter, Wizard): 
                                        First_fighter.print_mana()
                                print("--------------------------------")
                                attack_type = False
                                fight_condition = False
                            else :
                                    print("Vous n'avez pas choisi d'action valide")
                                    attack_type = False
                                    fight_condition = False

                    else:
                        print("Au revoir !")
                        break

        elif answers['choice_mode'] == 'Arena (vous etes en duel)':
            print("Vous avez choisi la classe Arena !")

            player_character_response = inquirer.prompt(game_questions.questions_character)
            player_character = player_character_response['choice_character']

            player_fighter_response = inquirer.prompt(game_questions.questions_fighter)
            player_fighter = player_fighter_response['choice_fighter']


            if player_fighter == 'Barbare (Attaque 2 fois)' or player_fighter == 'Sorcier (utilise des sorts)':
                if player_fighter == "Barbare (Attaque 2 fois)":
                    weapon_response = inquirer.prompt(game_questions.questions_weapon)
                    user_weapon = None
                    weapon_condition = True
                    player_selections.select_weapon(answers)
                    player = Barbarian(player_character, None, player_selections.user_weapon, 120)

                else:
                    spell_response = inquirer.prompt(game_questions.questions_spell)
                    user_spell = None
                    weapon_condition = True
                    player_selections.select_spell(answers)
                    player = Wizard(player_character, None, player_selections.user_spell, 75, fist_weapon, 60)


            bot_character = "Bot"
            bot_weapon = sword_weapon 
            bot = Barbarian(bot_character, None, bot_weapon, 100)  

            arena = Arena(player, bot)

            print(f"Vous affrontez {bot_character} dans l'arène !\n")

            arena.fight()

        
        elif answers['choice_mode'] == 'Histoire (vous vous battez contre des monstres)':
            print("Vous avez choisi la classe histoire !")            
            player_character_response = inquirer.prompt(game_questions.questions_character)
            player_character = player_character_response['choice_character']

            player_fighter_response = inquirer.prompt(game_questions.questions_fighter)
            player_fighter = player_fighter_response['choice_fighter']


            if player_fighter == 'Barbare (Attaque 2 fois)' or player_fighter == 'Sorcier (utilise des sorts)':
                if player_fighter == "Barbare (Attaque 2 fois)":
                    weapon_response = inquirer.prompt(game_questions.questions_weapon)
                    user_weapon = None
                    weapon_condition = True
                    player_selections.select_weapon(answers)
                    player = Barbarian(player_character, None, player_selections.user_weapon, 120)

                else:
                    spell_response = inquirer.prompt(game_questions.questions_spell)
                    user_spell = None
                    weapon_condition = True
                    player_selections.select_spell(answers)
                    player = Wizard(player_character, None, player_selections.user_spell, 75, fist_weapon, 60)

            monster_types = [Goblin, Dragon, Zombie, Ghost]

            map_size = 4
            game_map = Map(num_rooms=map_size)

            for i, room in enumerate(game_map.rooms, start=1):
                if player.hp <= 0:
                    print("Vous avez perdu. Fin du jeu.")
                    break
                
                if room.monster:
                    monster_type = random.choice(monster_types)
                    monster = monster_type(f"Monstre {i}", hp=random.randint(50, 100))
                    print(f"Salle {room.room_number}: {monster.name} ({monster.hp} HP)")
                    arena_monster = Arena(player, monster)
                    arena_monster.fight()

                    if player.hp <= 0:
                        print("Vous avez perdu. Fin du jeu.")
                        break
                    
                else:
                    print(f"Salle {room.room_number}: Le couloir")

            

        elif answers['choice_mode'] == 'Quitter':
            print("Vous n'avez pas choisi de mode !")
