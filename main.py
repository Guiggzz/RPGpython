class Personnage:
    def __init__(self, name: str, type_: str=None, HP:float=100, Shield:float=0, power:float=50):
        self.name = name
        self.HP = HP
        self.Shield = Shield
        self.power = power
        self.type_ = type_
    
    def jeu(self):
        while self.HP != 0:

            def attack(self, attack_type):
                if self.power > 0:
                    attack_type = input("Quelle attaque souhaitez vous faire ?")
                    if attack_type == "Hit 1":
                        print(f'{self.name} a donné un coup de poingts !\n')
                        self.power -= 5




Bordane = Personnage("Bordane", "Chevalier")
Bordane.jeu()

