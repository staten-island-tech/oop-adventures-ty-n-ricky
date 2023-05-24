
import random
inventory_apple = 1
inventory_bread = 1
inventory_pie = 1
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
def eat_food():
    which_eat = input("What do you want to eat? ")
    while inventory_apple > 0:
        if which_eat.capitalize() == "Apple":
            if Apple + player_hp > Max_hp:
                player_hp = Max_hp
                print(player_hp)
            else:
                player_hp = Apple + Max_hp
                print(player_hp)
    while inventory_bread > 0:
       if which_eat.capitalize() == "Bread":
          if Bread + player_hp > Max_hp:
                player_hp = Max_hp
                print(player_hp)
          else:
               player_hp = Bread + Max_hp
               print(player_hp)
    while inventory_pie > 0:
       if which_eat.capitalize() == "Pie":
          if Pie + player_hp > Max_hp:
                player_hp = Max_hp
                print(player_hp)
          else:
                player_hp = Pie + Max_hp
                print(player_hp)
def fight_skeleton():
    newhp = skeleton.hp - player.attack
    print(newhp, "health left")
    if newhp < 1:
        new_gold = gold + skeleton.gold_drop
        print("Your gold:", new_gold)
def fight_goblin():
    newhp = goblin.hp - player.attack
    print(newhp, "health left")
    if newhp < 1:
       new_gold = gold + goblin.gold_drop
       print("Your gold:", new_gold)
def fight_orc():
    newhp = orc.hp - player.attack
    print(newhp, "health left")
    if newhp < 1:
        new_gold = gold + orc.gold_drop
        print("Your gold:", new_gold)
def keep_fighting_skeleton():
    new_player_hp = player.hp - skeleton.attack
    print("Your hp",new_player_hp)
    keep_fight = input("Do you want to keep fighting? Y/N ")
    while keep_fight.capitalize() == "Y":
        fight_skeleton()
        keep_fight = input("Do you want to keep fighting? Y/N ")
def keep_fighting_goblin():
    new_player_hp = player.hp - goblin.attack
    print("Your hp",new_player_hp)
    keep_fight = input("Do you want to keep fighting? Y/N ")
    while keep_fight.capitalize() == "Y":
        fight_goblin()
        keep_fight = input("Do you want to keep fighting? Y/N ")
def keep_fighting_orc():
    new_player_hp = player.hp - orc.attack
    print("Your hp",new_player_hp)
    keep_fight = input("Do you want to keep fighting? Y/N ")
    while keep_fight.capitalize() == "Y":
        fight_orc()
        keep_fight = input("Do you want to keep fighting? Y/N ")




randoms = random.randint(1,3)
if randoms == 1:
    print("A wild skeleton appeared!")
    choose = input("What will you do? (Fight/Food/Run) ")
    if choose.capitalize() == "Fight":
       fight_skeleton()
       keep_fighting_skeleton()
    elif choose.capitalize() == "Food":
        which_eat = input("What do you want to eat? ")
        eat_food()
    elif choose.capitalize() == "Run":
        print("You fled")
    else:
        print("Something went wrong _(:з)∠)_")
elif randoms == 2:
    print("A wild goblin appeared!")
    choose = input("What will you do? (Fight/Food/Run) ")
    if choose.capitalize() == "Fight":
        fight_goblin()
        keep_fighting_goblin()
    elif choose.capitalize() == "Food":
           eat_food()
    elif choose.capitalize() == "Run":
           print("You fled")
    else:
           print("Something went wrong _(:з)∠)_")
elif randoms == 3:
    print("A wild orc appeared!")
    choose = input("What will you do? (Fight/Food/Run) ")
    if choose.capitalize() == "Fight":
       fight_orc()
       keep_fighting_orc()
    elif choose.capitalize() == "Food":
        eat_food()
    elif choose.capitalize() == "Run":
        print("You fled")
    else:
        print("Something went wrong _(:з)∠)_")
