class armor :
    def __init__(self, name: str, defense: float = 25):
        self.name = name
        self.defense = defense

    def armor_type(self):
        if self.name == 'armure partielle':
            self.defense = 50
            print (f"{self.name} choisie, vous avez {self.defense} points d'armure")
        elif self.name == 'armure moyenne':
            self.defense = 75
            print (f"{self.name} choisie, vous avez {self.defense} points d'armure")
        elif self.name == 'armure complète':
            self.defense = 100
            print (f"{self.name} choisie, vous avez {self.defense} points d'armure")
