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

class Shop():
   def apple_buy(player):
      how_much_apple = input("How many apples do you want to buy? ")
      player.gold = player.gold - (5 * int(how_much_apple))
      if player.gold >= 0:
         new_inventory_apple = int(inventory_apple) + int(how_much_apple)
         print("Your gold", player.gold)
         print("Your apple", new_inventory_apple)
         """ return y """
      else:
         print("Not enough gold")
   def bread_buy(player):
      how_much_bread = input("How many bread do you want to buy? ")
      player.gold = player.gold - (20 * int(how_much_bread))
      if player.gold >= 0:
         new_inventory_bread = int(inventory_bread) + int(how_much_bread)
         print("Your gold", player.gold)
         print("Your bread", new_inventory_bread)
      else:
         print("Not enough gold")
   def pie_buy(player):
      how_much_pie = input("How many pie do you want to buy? ")
      player.gold = player.gold - (50 * int(how_much_pie))
      if player.gold >= 0:
         new_inventory_pie = int(inventory_pie) + int(how_much_pie)
         print("Your gold", player.gold)
         print("Your pie", new_inventory_pie)
      else:
            print("Not enough gold")
   def buy_bronze(player, y):
      player.gold = player.gold - 30
      if player.gold >= 0:
         new_inventory_bronze = int(inventory_bronze) +1
         y.append("bronze")
         print("Your gold", player.gold)
         print("Your bronze", new_inventory_bronze)
   def buy_iron(player, y):
      player.gold = player.gold - 50
      if player.gold >= 0:
         new_inventory_iron = int(inventory_iron) + 1
         y.append("iron")
         print("Your gold", player.gold)
         print("Your iron", new_inventory_iron)
   def buy_steel(player, y):
      player.gold = player.gold - 100
      if player.gold >= 0:
         new_inventory_steel = int(inventory_steel) + 1
         y.append("steel")
         print("Your gold", player.gold)
         print("Your steel", new_inventory_steel)
   def buy_sword(player, x):
      player.gold = player.gold - 10
      if player.gold >= 0:
         new_inventory_sword = int(inventory_sword) + 1
         x.append("sword")
         print("You gold",player.gold)
         print("Your sword",new_inventory_sword)
   def buy_sledge(player, x):
      player.gold = player.gold - 25
      if player.gold >= 0:
         new_inventory_sledgehammer = int(inventory_sledgehammer) + 1
         x.append("sledgehammer")
         print(x)
         print("Your gold",player.gold)
         print("Your sledgehammer", new_inventory_sledgehammer)
   def buy_axe(player, x):
      player.gold = player.gold - 50
      if player.gold >= 0:
         new_inventory_axe = inventory_axe + 1
         x.append("axe")
         print(x)
         print("Your gold",player.gold)
         print("Your axe",new_inventory_axe)
   def buy_scythe(player, x):
      player.gold = player.gold - 100
      if player.gold >= 0:
         new_inventory_scythe = int(inventory_scythe) +1
         x.append("scythe")
         print(x)
         print("Your gold",player.gold)
         print("Your scythe",new_inventory_scythe)   
   def shop(self,x):
         what_buy = input("What do you want to buy? (Food,Armor,Weapon) ")
         if what_buy.capitalize() == "Food":
            which_food = input("which food? (Apple($5 ,20 heal)/Bread($20 ,50 heal)/Pie($50 ,100 heal)) ")
            if which_food.capitalize() == "Apple":  
               self.apple_buy()
            if which_food.capitalize() == "Bread":
               self.bread_buy()
            if which_food.capitalize() == "Pie":  
               self.pie_buy()
         elif what_buy.capitalize() == "Armor":
            which_armor = input("Which armor? (bronze($30, 20 hp)/iron($50, 35 hp)/steel($100, 50 hp)) ")
            if which_armor.capitalize() == "Bronze":  
               self.buy_bronze()
            if which_armor.capitalize() == "Iron":  
               self.buy_iron()
            if which_armor.capitalize() == "Steel":  
               self.buy_steel()
         elif what_buy.capitalize() == "Weapon":
            which_weapon = input("Which weapon? (sword($10, 15 dmg)/sledgehammer($20, 30 dmg)/axe($50, 50 dmg)/scythe(100$, 75 dmg) ")
            if which_weapon.capitalize() == "Sword":
               self.buy_sword()
            if which_weapon.capitalize() == "Sledgehammer":
               self.buy_sledge()
            if which_weapon.capitalize() == "Axe":
               self.buy_axe()
            if which_weapon.capitalize() == "Scythe":
               self.buy_scythe()
# continue_shop = input("Would you like to keep shopping? Y/N 💖 ")
# while continue_shop.upper() == "Y":
#    if continue_shop.upper() == 'Y':
      
#     continue_shop = input("Would you like to keep shopping? Y/N 💖 ")



