class PlayerSelection:
    def __init__(self):
        self.user_weapon = None
        self.user_armor = None
        self.user_spell = None
        self.weapon_condition = True
        self.armor_condition = True

    def select_weapon(self, choice):
        if choice == 'Épée (30 dps)':
            self.user_weapon = sword_weapon
        elif choice == 'Pioche (25 dps)':
            self.user_weapon = pickaxe_weapon
        elif choice == 'Coup de poing (20 dps)':
            self.user_weapon = fist_weapon
        else:
            self.weapon_condition = False

    def select_armor(self, choice):
        if choice == "Armure légère (50 de défense)":
            self.user_armor = little_armor
        elif choice == "Armure moyenne (75 de défense)":
            self.user_armor = mid_armor
        elif choice == "Armure complète (100 de défense)":
            self.user_armor = complete_armor
        else:
            self.armor_condition = False

    def select_spell(self, choice):
        if choice == 'Boule de feu (50 dps)':
            self.user_spell = fireball_spell
        elif choice == 'Tonerre (45 dps)':
            self.user_spell = lightning_spell
        elif choice == "Mur d'air (30 dps)":
            self.user_spell = windwall_spell
        else:
            self.weapon_condition = False
