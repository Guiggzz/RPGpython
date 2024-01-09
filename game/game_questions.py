import inquirer

class GameQuestions:
    def __init__(self):
        self.questions_mode = [
            inquirer.List('choice_mode',
                          message="Sélectionnez un mode de jeu ",
                          choices=['Histoire (vous vous battez contre des monstres)', 'Arena (vous etes en duel)', 'Punching-Ball (vous etes le seul a attaquer)', 'Quitter'],
                      ),
        ]
        self.questions_character = [
            inquirer.List('choice_character',
                          message="Sélectionnez un character ",
                          choices=['Bordan', 'Marleine', 'Zizou', 'Shappa', 'M', 'Quitter'],
                      ),
        ]
        self.questions_fighter = [
            inquirer.List('choice_fighter',
                          message="Sélectionnez un attribu",
                          choices=['Barbare (Attaque 2 fois)', 'Sorcier (utilise des sorts)', 'Quitter'],
                      ),
        ]
        self.questions_weapon = [
            inquirer.List('choice_weapon',
                          message="Sélectionnez une arme ",
                          choices=['Épée (30 dps)', 'Pioche (25 dps)', 'Coup de poing (20 dps)', 'Quitter'],
                      ),
        ]
        self.questions_armor = [
            inquirer.List('choice_armor',
                          message="Sélectionnez une armure ",
                          choices=['Armure légère (50 de défense)', 'Armure moyenne (75 de défense)', 'Armure complète (100 de défense)', 'Quitter'],
                      ),
        ]
        self.questions_fight = [
            inquirer.List('choice_fight',
                          message="Voulez-vous attaquer ? ",
                          choices=['Oui', 'Non', 'Quitter'],
                      ),
        ]
        self.questions_spell = [
            inquirer.List('choice_spell',
                          message="Sélectionnez un sort ",
                          choices=['Boule de feu (50 dps)', 'Tonerre (45 dps)', "Mur d'air (30 dps)", 'Quitter'],
                      ),
        ]

