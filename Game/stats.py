class Player():
    def __init__(self, hp, attack ):
        self.hp = hp
        self.attack = attack
class Mobs(Player):
    def __init__(self, hp, attack, gold_drop):
        super().__init__(hp, attack)
        self.gold_drop = gold_drop
player = Player(100, 5)
skeleton = Mobs(30, 20, 2)
goblin = Mobs(50, 10, 2)
orc = Mobs(75, 5, 3)


def weapon_inventory():
    list = ["sword", "dagger", "hammer"]
    in_use_weapon = input("What weapon do you want to equip?: ").lower()
    if in_use_weapon in list:
        print("equipped", in_use_weapon)
    else:
        print("You don't have that")

# class Inventory():
#     def __init__(self, weapon, food, gold, armor):
#         self.weapon = weapon
#         self.food = food
#         self.gold = gold
#         self.armor = armor
#     def __str__ (self):

# inventory = Inventory(weapon_inventory, )
# print(inventory)


