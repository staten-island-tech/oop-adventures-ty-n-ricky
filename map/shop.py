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
gold = 100
def shop():
       what_buy = input("What do you want to buy? (Food,Armor,Weapon) ")
       if what_buy.capitalize() == "Food":
          which_food = input("which food? (Apple($5 ,20 energy,20 heal)/Bread($20 ,50 energy,50 heal)/Pie($50 ,100 energy,100 heal)) ")
          if which_food.capitalize() == "Apple":  
            how_much_apple = input("How many apples do you want to buy? ")
            new_gold = gold - (5 * int(how_much_apple))
            if new_gold >= 0: 
               new_inventory_apple = int(inventory_apple) + int(how_much_apple)
               print("Your gold", new_gold)
               print("Your apple", new_inventory_apple)
            else: 
               print("Not enough gold")
          if which_food.capitalize() == "Bread":   
            how_much_bread = input("How many bread do you want to buy? ")
            new_gold = gold - (20 * int(how_much_bread))
            if new_gold >= 0: 
               new_inventory_bread = int(inventory_bread) + int(how_much_bread)
               print("Your gold", new_gold)
               print("Your bread", new_inventory_bread)
            else: 
                print("Not enough gold")
          if which_food.capitalize() == "Pie":  
            how_much_pie = input("How many pie do you want to buy? ")
            new_gold = gold - (50 * int(how_much_pie))
            if new_gold >= 0:
               new_inventory_pie = int(inventory_pie) + int(how_much_pie)
               print("Your gold", new_gold)
               print("Your pie", new_inventory_pie)
            else: 
                   print("Not enough gold")
       elif what_buy.capitalize() == "Armor":
          which_armor = input("Which armor? (bronze($30, 20 hp)/iron($50, 35 hp)/steel($100, 50 hp)) ")
          if which_armor.capitalize() == "Bronze":   
            new_gold = gold - 30 
            if new_gold >= 0: 
               new_inventory_bronze = int(inventory_bronze) +1
               print("Your gold", new_gold)
               print("Your bronze", new_inventory_bronze)
          if which_armor.capitalize() == "Iron":   
            new_gold = gold - 50
            if new_gold >= 0: 
               new_inventory_iron = int(inventory_iron) + 1
               print("Your gold", new_gold)
               print("Your iron", new_inventory_iron)
          if which_armor.capitalize() == "Steel":   
            new_gold = gold - 100 
            if new_gold >= 0: 
               new_inventory_steel = int(inventory_steel) + 1
               print("Your gold", new_gold)
               print("Your steel", new_inventory_steel)
       elif what_buy.capitalize() == "Weapon":
         which_weapon = input("Which weapon? (sword($10, 15 dmg)/sledgehammer($20, 30 dmg)/axe($50, 50 dmg)/scythe(100$, 75 dmg) ")
         if which_weapon.capitalize() == "Sword":
            new_gold = gold - 10 
            if new_gold >= 0: 
               new_inventory_sword = int(inventory_sword) + 1
               print("You gold",new_gold)
               print("Your sword",new_inventory_sword)
         if which_weapon.capitalize() == "Sledgehammer":
            new_gold = gold - 25 
            if new_gold >= 0: 
               new_inventory_sledgehammer = int(inventory_sledgehammer) + 1
               print("Your gold",new_gold)
               print("Your sledgehammer", new_inventory_sledgehammer)
         if which_weapon.capitalize() == "Axe":
            new_gold = gold - 50 
            if new_gold >= 0: 
               new_inventory_axe = inventory_axe + 1
               print("Your gold",new_gold)
               print("Your axe",new_inventory_axe)
         if which_weapon.capitalize() == "Scythe":
            new_gold = gold - 100 
            if new_gold >= 0: 
               new_inventory_scythe = int(inventory_scythe) +1
               print("Your gold",new_gold)
               print("Your scythe",new_inventory_scythe)
shop()
continue_shop = input("Would you like to keep shopping? Y/N ")
while continue_shop.upper() == "Y":
    shop()
    continue_shop = input("Would you like to keep shopping? Y/N ")