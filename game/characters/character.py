from gears.armor import armor
from gears.weapon import weapon

class Character(armor, weapon):
    def __init__(self):
        super().__init__()
    def __init__(self, name: str, armor,  weapon: str = 'Le saint batôn de berger',  hp: float = 100 ):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.hp = hp



    