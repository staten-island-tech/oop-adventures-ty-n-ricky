from dungeon import Player, Mobs
from shop import Shop
from dungeon import Dungeon 
from inventory import Weapons
from inventory import Armors
from inventory import Inventory
#initialize dungeon classes
player = Player(100, 5, 0)
skeleton = Mobs(30, 20, 2, 0)
goblin = Mobs(50, 10, 2, 0)
orc = Mobs(75, 5, 3, 0)

inventory = Inventory(Weapons.in_use_weapon, 0, 0, 0, 0, Armors.in_use_armor)
print("weapon:", inventory.weapon, "gold:", inventory.gold, "apple:", inventory.apple, "bread:", inventory.bread, "pie:", inventory.pie, "armor:", inventory.armor)

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

shop=Shop()
shop.shop(player)
which_map = input("Where do you want to travel? (Shop,Dungeon) ")
if which_map.capitalize() == "Shop":
  what_buy = input("What do you want to buy? (Food,Armor,Weapon) ")
  if what_buy.capitalize() == "Food":
            which_food = input("which food? (Apple($5 ,20 heal)/Bread($20 ,50 heal)/Pie($50 ,100 heal)) ")
            if which_food.capitalize() == "Apple":  
               Shop.apple_buy()
            if which_food.capitalize() == "Bread":
               Shop.bread_buy()
            if which_food.capitalize() == "Pie":  
               Shop.pie_buy()
  elif what_buy.capitalize() == "Armor":
            which_armor = input("Which armor? (bronze($30, 20 hp)/iron($50, 35 hp)/steel($100, 50 hp)) ")
            if which_armor.capitalize() == "Bronze":  
               Shop.buy_bronze()
            if which_armor.capitalize() == "Iron":  
               Shop.buy_iron()
            if which_armor.capitalize() == "Steel":  
               Shop.buy_steel()
  elif what_buy.capitalize() == "Weapon":
            which_weapon = input("Which weapon? (sword($10, 15 dmg)/sledgehammer($20, 30 dmg)/axe($50, 50 dmg)/scythe(100$, 75 dmg) ")
            if which_weapon.capitalize() == "Sword":
               Shop.buy_sword()
            if which_weapon.capitalize() == "Sledgehammer":
               Shop.buy_sledge()
            if which_weapon.capitalize() == "Axe":
               Shop.buy_axe()
            if which_weapon.capitalize() == "Scythe":
               Shop.buy_scythe()
elif which_map.capitalize() == "Dungeon":
  print("iuasgdfuolhj")





