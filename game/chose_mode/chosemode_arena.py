from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapon
from characters.Barbarian import Barbarian
from characters.wizard import Wizard
from gears.spell import Spell
from arena import Arena
import time
import inquirer
from game_questions import GameQuestions

def arena_mode(game_questions, player_selections, answers, fist_weapon, sword_weapon):
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
