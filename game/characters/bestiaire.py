# import random
# from characters.character import Character
# from gears.armor import Armor
# from gears.weapon import Weapon
# little_armor = Armor('armure partielle', 50)
# mid_armor = Armor('armure moyenne', 75)
# complete_armor = Armor('armure complète', 100)

# sword_weapon = Weapon('Épée', 30)
# pickaxe_weapon = Weapon('Pioche', 25)
# fist_weapon = Weapon('Coup de poing', 20)

# class Monster(Character):
#     def __init__(self, name, hp, armor, weapon, monster_type):
#         super().__init__(name, armor, weapon, hp=hp)
#         self.monster_type = monster_type

# class Boss(Monster):
#     def __init__(self, name='boss', hp: float = 500, monster_type="Boss"):
#         super().__init__(name, hp=hp, monster_type=monster_type)

# class Zombie(Monster):
#     def __init__(self, name='zombie', armor=None, weapon=None, hp=50):
#         super().__init__(name, armor, weapon, hp=hp)

# class Goblin(Monster):
#     def __init__(self, name='goblin', armor=None, weapon=None, hp=75):
#         super().__init__(name, armor, weapon, hp=hp)

# class Dragon(Monster):
#     def __init__(self, name='dragon', armor=None, weapon=None, hp=150):
#         super().__init__(name, armor, weapon, hp=hp)

# class Ghost(Monster):
#     def __init__(self, name='ghost', armor=None, weapon=None, hp=100):
#         super().__init__(name, armor, weapon, hp=hp)

# # Assign names to your instances
# zombiename = Zombie('Zombie', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))
# goblinname = Goblin('Goblin', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))
# dragonname = Dragon('Dragon', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))
# ghostname = Ghost('Ghost', random.choice((little_armor, mid_armor, complete_armor)), random.choice((sword_weapon, pickaxe_weapon, fist_weapon)))

# class Room:
#     def __init__(self, room_number, monster=None):
#             self.room_number = room_number
#             self.monster = monster
# class Map:
#     def __init__(self, num_rooms):
#             self.num_rooms = num_rooms
#             self.rooms = []
#             self.generate_map()
#     def generate_map(self):
#             monster_types = [Zombie, Goblin, Dragon, Ghost, Boss]
            
#             for i in range(1, self.num_rooms):
#                 monster_type = random.choice(monster_types)
#                 monster = monster_type(f"Monstre {i}", hp=random.randint(50, 100))
#                 room = Room(room_number=i, monster=monster)
#                 self.rooms.append(room)

#             boss = Boss("Monstre C (Boss)", hp=random.randint(150, 200), monster_type="Boss")
#             boss_room = Room(room_number=self.num_rooms, monster=boss)
#             self.rooms.append(boss_room)
# monster_types = [Zombie, Goblin, Dragon, Ghost, Boss]
