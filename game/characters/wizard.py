class wizard : 
    def __init__(self, hp = 75, sorts = None, mana = 50 ):
        self.hp = hp
        self.sorts = sorts
        self. mana = mana

class spell:
    def __init__(self,name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana = mana_cost
    