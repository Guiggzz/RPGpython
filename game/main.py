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
from modeSelection import ModeSelections
mode_selections = ModeSelections()

mode_selections.select_mode(ModeSelections)