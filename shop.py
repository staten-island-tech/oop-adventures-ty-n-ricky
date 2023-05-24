
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
gold = {"gold": 100}


def apple_buy():
   how_much_apple = input("How many apples do you want to buy? ")
   new_gold = int(gold) - (5 * int(how_much_apple))
   if new_gold >= 0:
      new_inventory_apple = int(inventory_apple) + int(how_much_apple)
      print("Your gold", new_gold)
      print("Your apple", new_inventory_apple)
   else:
      print("Not enough gold")
def bread_buy():
   how_much_bread = input("How many bread do you want to buy? ")
   new_gold = gold - (20 * int(how_much_bread))
   if new_gold >= 0:
      new_inventory_bread = int(inventory_bread) + int(how_much_bread)
      print("Your gold", new_gold)
      print("Your bread", new_inventory_bread)
   else:
       print("Not enough gold")
def pie_buy():
   how_much_pie = input("How many pie do you want to buy? ")
   new_gold = gold - (50 * int(how_much_pie))
   if new_gold >= 0:
      new_inventory_pie = int(inventory_pie) + int(how_much_pie)
      print("Your gold", new_gold)
      print("Your pie", new_inventory_pie)
   else:
          print("Not enough gold")
def buy_bronze():
   new_gold = gold - 30
   if new_gold >= 0:
      new_inventory_bronze = int(inventory_bronze) +1
      print("Your gold", new_gold)
      print("Your bronze", new_inventory_bronze)
def buy_iron():
   new_gold = gold - 50
   if new_gold >= 0:
      new_inventory_iron = int(inventory_iron) + 1
      print("Your gold", new_gold)
      print("Your iron", new_inventory_iron)
def buy_steel():
   new_gold = gold - 100
   if new_gold >= 0:
      new_inventory_steel = int(inventory_steel) + 1
      print("Your gold", new_gold)
      print("Your steel", new_inventory_steel)
def buy_sword():
   new_gold = gold["gold"] - 10
   gold.update({'gold':new_gold})
   if new_gold >= 0:
      new_inventory_sword = int(inventory_sword) + 1
      weapons.append("sword")
      print(weapons)
      print("You gold",new_gold)
      print("Your sword",new_inventory_sword)
def buy_sledge():
   new_gold = gold - 25
   if new_gold >= 0:
      new_inventory_sledgehammer = int(inventory_sledgehammer) + 1
      weapons.append("sledgehammer")
      print(weapons)
      print("Your gold",new_gold)
      print("Your sledgehammer", new_inventory_sledgehammer)
def buy_axe():
   new_gold = gold - 50
   if new_gold >= 0:
      new_inventory_axe = inventory_axe + 1
      weapons.append("axe")
      print(weapons)
      print("Your gold",new_gold)
      print("Your axe",new_inventory_axe)
def buy_scythe():
   new_gold = gold - 100
   if new_gold >= 0:
      new_inventory_scythe = int(inventory_scythe) +1
      weapons.append("scythe")
      print(weapons)
      print("Your gold",new_gold)
      print("Your scythe",new_inventory_scythe)


def shop():
       what_buy = input("What do you want to buy? (Food,Armor,Weapon) ")
       if what_buy.capitalize() == "Food":
          which_food = input("which food? (Apple($5 ,20 heal)/Bread($20 ,50 heal)/Pie($50 ,100 heal)) ")
          if which_food.capitalize() == "Apple":  
            apple_buy()
          if which_food.capitalize() == "Bread":
            bread_buy()
          if which_food.capitalize() == "Pie":  
            pie_buy()
       elif what_buy.capitalize() == "Armor":
          which_armor = input("Which armor? (bronze($30, 20 hp)/iron($50, 35 hp)/steel($100, 50 hp)) ")
          if which_armor.capitalize() == "Bronze":  
           buy_bronze()
          if which_armor.capitalize() == "Iron":  
            buy_iron()
          if which_armor.capitalize() == "Steel":  
            buy_steel()
       elif what_buy.capitalize() == "Weapon":
         which_weapon = input("Which weapon? (sword($10, 15 dmg)/sledgehammer($20, 30 dmg)/axe($50, 50 dmg)/scythe(100$, 75 dmg) ")
         if which_weapon.capitalize() == "Sword":
           buy_sword()
         if which_weapon.capitalize() == "Sledgehammer":
            buy_sledge()
         if which_weapon.capitalize() == "Axe":
            buy_axe()
         if which_weapon.capitalize() == "Scythe":
            buy_scythe()
shop()
continue_shop = input("Would you like to keep shopping? Y/N 💖 ")
while continue_shop.upper() == "Y":
    shop()
    continue_shop = input("Would you like to keep shopping? Y/N 💖 ")




