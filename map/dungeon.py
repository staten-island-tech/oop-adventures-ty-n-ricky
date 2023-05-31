import random
inventory_apple = 1
inventory_bread = 1
inventory_pie = 1
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
    def __init__(self, hp, attack, gold):
        self.hp = hp
        self.attack = attack
        self.gold = gold
class Mobs(Player):
    def __init__(self, hp, attack, gold_drop, gold):
        super().__init__(hp, attack, gold)
        self.gold_drop = gold_drop
player = Player(100, 5, 0)
skeleton = Mobs(30, 20, 2, 0)
goblin = Mobs(50, 10, 2, 0)
orc = Mobs(75, 5, 3, 0)


def eat_food():
    which_eat = input("What food do you want to eat? (Apple, Bread, Pie) ")
    if inventory_apple > 0:
        if which_eat.capitalize() == "Apple":
            if Apple + player.hp > Max_hp:
                player.hp = Max_hp
                print("Your health",player.hp)
            else:
                player.hp = Apple + player.hp
                print("Your health",player.hp)
    if inventory_bread > 0:
       if which_eat.capitalize() == "Bread":
          if Bread + player.hp > Max_hp:
                player.hp = Max_hp
                print("Your health",player.hp)
          else:
               player.hp = Bread + player.hp
               print("Your health",player.hp)
    if inventory_pie > 0:
       if which_eat.capitalize() == "Pie":
          if Pie + player.hp > Max_hp:
                player.hp = Max_hp
                print("Your health",player.hp)
          else:
                player.hp = Pie + player.hp
                print("Your health",player.hp)
def fight_skeleton():
    skeleton.hp = skeleton.hp - player.attack
    print(skeleton.hp, "health left")
    if skeleton.hp < 1:
        player.gold = player.gold + skeleton.gold_drop
        print("Your gold:", player.gold)
    player.hp = player.hp - skeleton.attack
    print(player.hp,"Your health")
    if player.hp < 1:
        print("You died")
def fight_goblin():
    goblin.hp = goblin.hp - player.attack
    print(goblin.hp, "health left")
    if goblin.hp < 1:
       player.gold = player.gold + goblin.gold_drop
       print("Your gold:", player.gold)
    player.hp = player.hp - goblin.attack
    print(player.hp,"Your health")
    if player.hp < 1:
        print("You died")
def fight_orc():
    orc.hp = orc.hp - player.attack
    print(orc.hp, "health left")
    if orc.hp < 1:
        player.gold = player.gold + orc.gold_drop
        print("Your gold:", player.gold)
    player.hp = player.hp - orc.attack
    print(player.hp,"Your health")
    if player.hp < 1:
        print("You died")
def continue_fight_skeleton():
    continues = input("Do you want to continue the fight? Y/N ")
    while continues.capitalize() == "Y" and skeleton.hp > 1:
       next = input("What will you do next? (Fight/Food/Flee) ")
       if next.capitalize() == "Food":
           eat_food()
       elif next.capitalize() == "Fight":
           fight_skeleton()
       elif next.capitalize() == "Flee":
           print("You fled")
           break
       else:
           print("Something went wrong _(:з)∠)_")
       continues = input("Do you want to continue the fight? Y/N ")
def continue_fight_goblin():
    continues = input("Do you want to continue the fight? Y/N ")
    while continues.capitalize() == "Y" and goblin.hp > 1:
       next = input("What will you do next? (Fight/Food/Flee) ")
       if next.capitalize() == "Food":
           eat_food()
       elif next.capitalize() == "Fight":
           fight_goblin()
       elif next.capitalize() == "Flee":
           print("You fled")
           break
       else:
           print("Something went wrong _(:з)∠)_")
       continues = input("Do you want to continue the fight? Y/N ")
def continue_fight_orc():
    continues = input("Do you want to continue the fight? Y/N ")
    while continues.capitalize() == "Y" and orc.hp > 1:
       next = input("What will you do next? (Fight/Food/Flee) ")
       if next.capitalize() == "Food":
           eat_food()
       elif next.capitalize() == "Fight":
           fight_orc()
       elif next.capitalize() == "Flee":
           print("You fled")
           break
       else:
           print("Something went wrong _(:з)∠)_")
       continues = input("Do you want to continue the fight? Y/N ")
randoms = random.randint(1,3)
if randoms == 1:
    print("A wild skeleton appeared!")
    choose = input("What will you do? (Fight/Food/Flee) ")
    if choose.capitalize() == "Fight":
       fight_skeleton()
       continue_fight_skeleton()
    elif choose.capitalize() == "Food":
        eat_food()
    elif choose.capitalize() == "Flee":
        print("You fled")
    else:
        print("Something went wrong _(:з)∠)_")
elif randoms == 2:
    print("A wild goblin appeared!")
    choose = input("What will you do? (Fight/Food/Run) ")
    if choose.capitalize() == "Fight":
        fight_goblin()
        continue_fight_goblin()
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
       continue_fight_orc()
    elif choose.capitalize() == "Food":
        eat_food()
    elif choose.capitalize() == "Run":
        print("You fled")
    else:
        print("Something went wrong _(:з)∠)_")