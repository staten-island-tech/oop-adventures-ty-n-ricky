from dungeon import Player, Mobs
from shop import Shop
from dungeon import Dungeon 
# from inventory import Weapons
# from inventory import Armors
# from inventory import Inventory
#initialize dungeon classes
player = Player(100, 5, 0)
skeleton = Mobs(30, 20, 2, 0)
goblin = Mobs(50, 10, 2, 0)
orc = Mobs(75, 5, 3, 0)

# inventory = Inventory(Weapons.in_use_weapon, 0, 0, 0, 0, Armors.in_use_armor)
# print("weapon:", inventory.weapon, "gold:", inventory.gold, "apple:", inventory.apple, "bread:", inventory.bread, "pie:", inventory.pie, "armor:", inventory.armor)

weapons = []
inventory_apple = 0
inventory_bread = 0
inventory_pie = 0
inventory_bronze = 0
inventory_iron = 0
inventory_steel = 0
inventory_sword = 0
inventory_sledgehammer = 0
inventory_axe = 0
inventory_scythe = 0

which_map = input("Where do you want to travel? (Shop,Dungeon) ")
continue_shop = input("Would you like to keep shopping? Y/N 💖 ")
if which_map.capitalize() == "Shop":
      shop=Shop()
      shop.shop(player)
elif which_map.capitalize() == "Dungeon":
  print("iuasgdfuolhj")





