def inventoryyyyy():
        bob = bob



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


class Weapon:
     def __init__(self, damage, cost):
            self.damage = damage
            self.cost = cost




class Inventory():
    def __init__(self, weapon, apple, bread, pie, gold, armor):
        self.weapon = weapon
        self.apple = apple
        self.bread = bread
        self.pie = pie
        self.gold = gold
        self.armor = armor       
inventory = Inventory(in_use_weapon, 0, 0, 0, 0, in_use_armor)
print("weapon:", inventory.weapon, "gold:", inventory.gold, "apple:", inventory.apple, "bread:", inventory.bread, "pie:", inventory.pie, "armor:", inventory.armor)
