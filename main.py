import random
inventory_apple = 1
inventory_bread = 1
inventory_pie = 1
game_hp = {"hp", 100}
real_hp = 100
Max_hp = 100
Apple = 20
Bread = 50
Pie = 100
gold = 0
class Weapon:
     def __init__(self, damage, cost):
            self.damage = damage
            self.cost = cost
knife = Weapon(0, 10)
sword = Weapon(10, 15)
sledgehammer = Weapon(25, 30)
axe = Weapon(50,50)
scythe = Weapon(100, 75)


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

def goblins():
  while real_hp > 0 and real_hp <= 100:
   new_hp = real_hp - goblin.attack
   game_hp.update(int(new_hp))
   print(game_hp)
goblins()
  


