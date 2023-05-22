def inventoryyyyy():
        
        weapon_list = []  
armor_list = []



weapon_list = ["sword", "dagger", "hammer"]
in_use_weapon = input("What weapon do you want to equip?: ").lower()
if in_use_weapon in weapon_list:
        print("equipped", in_use_weapon)
else:
        print("You don't have that")


armor_list = ["bronze", "iron", "steel"]
in_use_armor = input("What armor do you want to equip?: ").lower()
if in_use_armor in armor_list:
        print("equipped", in_use_armor)
else:
        print("You don't have that")

food_list = {"apple": 1, "bread": 10, "pie": 0}


gold_list = {"gold": 100}
class Weapon:
     def __init__(self, damage, cost):
            self.damage = damage
            self.cost = cost
knife = Weapon(0, 10)
sword = Weapon(10, 15)
sledgehammer = Weapon(25, 30)
axe = Weapon(50,50)
scythe = Weapon(100, 75)
new_gold = gold_list["gold"] - knife.cost
gold_list.update({"gold": new_gold})
new_gold = gold_list["gold"] - knife.cost
gold_list.update({"gold": new_gold})
inventory_gold = gold_list["gold"]


class Inventory():
    def __init__(self, weapon, apple, bread, pie, gold, armor):
        self.weapon = weapon
        self.apple = apple
        self.bread = bread
        self.pie = pie
        self.gold = gold
        self.armor = armor       
inventory = Inventory(in_use_weapon, food_list["apple"], food_list["bread"], food_list["pie"], inventory_gold, in_use_armor)
print("weapon:", inventory.weapon, "gold:", inventory.gold, "apple:", inventory.apple, "bread:", inventory.bread, "pie:", inventory.pie, "armor:", inventory.armor)
