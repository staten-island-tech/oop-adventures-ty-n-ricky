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
    def __init__(self, hp, attack, gold, sword, armor, apple, bread, pie):
        self.hp = hp
        self.attack = attack
        self.gold = gold
        self.sword = sword
        self.sledgehammer = sledgehammer
        self.axe = axe
        self.scythe = scythe
        self.bronze = bronze
        self.iron = 
        self.armor = armor
        self.apple = apple
        self.bread = bread
        self.pie = pie

class Mobs(Player):
    def __init__(self, hp, attack, gold_drop, gold):
        super().__init__(hp, attack, gold)
        self.gold_drop = gold_drop
player = Player(100, 5, 0)
skeleton = Mobs(30, 20, 2, 0)
goblin = Mobs(50, 10, 2, 0)
orc = Mobs(75, 5, 3, 0)

class Dungeon():
    def eat_food(player):
        which_eat = input("What food do you want to eat? (Apple, Bread, Pie) ")
        if inventory_apple > 0:
            if which_eat.capitalize() == "Apple":
                if Apple + player.hp > Max_hp:
                    player.hp = Max_hp
                    print("Your health",player.hp)
                else:
                    player.hp = Apple + Max_hp
                    print("Your health",player.hp)
        if inventory_bread > 0:
            if which_eat.capitalize() == "Bread":
                if Bread + player.hp > Max_hp:
                    player.hp = Max_hp
                    print("Your health",player.hp)
            else:
                player.hp = Bread + Max_hp
                print("Your health",player.hp)
        if inventory_pie > 0:
            if which_eat.capitalize() == "Pie":
                if Pie + player.hp > Max_hp:
                    player.hp = Max_hp
                    print("Your health",player.hp)
            else:
                    player.hp = Pie + Max_hp
                    print("Your health",player.hp)
    def fight_skeleton():
        skeleton.hp = skeleton.hp - player.attack
        print(skeleton.hp, "mob health left")
        player.hp = player.hp - skeleton.attack
        print(player.hp, "player health left")
        if skeleton.hp < 1:
            player.gold = player.gold + skeleton.gold_drop
            print("Your gold:", player.gold)
    def fight_goblin():
        goblin.hp = goblin.hp - player.attack
        print(goblin.hp, "mob health left")
        player.hp = player.hp - goblin.attack
        print(player.hp, "player health left")
        if goblin.hp < 1:
            player.gold = player.gold + goblin.gold_drop
        print("Your gold:", player.gold)
    def fight_orc():
        orc.hp = orc.hp - player.attack
        print(orc.hp, "mob health left")
        player.hp = player.hp - orc.attack
        print(player.hp, "player health left")
        if orc.hp < 1:
            player.gold = player.gold + orc.gold_drop
    #         print("Your gold:", player.gold)
    # def continue_fight_skeleton():
    #     next = input("What will you do next? (Fight/Food/Flee) ")
    #     while next.capitalize() != "Flee" and skeleton.hp > 0 and player.hp > 0:
    #         if skeleton.hp > 0 or player.hp > 0:
    #             if next.capitalize() == "Food":
    #                 eat_food()
    #                 next = input("What will you do next? (Fight/Food/Flee) ")
    #             elif next.capitalize() == "Fight":
    #                 fight_skeleton()
    #                 next = input("What will you do next? (Fight/Food/Flee) ")
    #             elif next.capitalize() == "Flee":
    #                 print("You fled")
    #             else: 
    #                 print("Something went wrong _(:з)∠)_")
    #         if skeleton.hp <= 0:
    #             print("you defeated the skeleton")
    #         if player.hp <= 0:
    #             print("you died")
    # def continue_fight_goblin():
    #     next = input("What will you do next? (Fight/Food/Flee) ")
    #     if next.capitalize() == "Food":
    #         eat_food()
    #     elif next.capitalize() == "Fight":
    #         fight_goblin()
    #     elif next.capitalize() == "Flee":
    #         print("You fled")
    #     else: 
    #         print("Something went wrong _(:з)∠)_")
    # def continue_fight_orc():
    #     next = input("What will you do next? (Fight/Food/Flee) ")
    #     if next.capitalize() == "Food":
    #         eat_food()
    #     elif next.capitalize() == "Fight":
    #         fight_orc()
    #     elif next.capitalize() == "Flee":
    #         print("You fled")
    #     else: 
    #         print("Something went wrong _(:з)∠)_")




""" randoms = random.randint(1,3)
if randoms == 1:
    print("A wild skeleton appeared!")
    choose = input("What will you do? (Fight/Food/Run) ")
    if choose.capitalize() == "Fight":
       fight_skeleton()
       continue_fight_skeleton()
    elif choose.capitalize() == "Food":
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


 """