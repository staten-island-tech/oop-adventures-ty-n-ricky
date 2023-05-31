inventory_apple = 1
inventory_bread = 1
inventory_pie = 1
Max_hp = 100
player_hp = 100
Apple = 20
Bread = 50
Pie = 100
which_eat = input("What food do you want to eat? (Apple, Bread, Pie) ")
if inventory_apple > 0:
    if which_eat.capitalize() == "Apple":
        if Apple + player_hp > Max_hp:
            player_hp = Max_hp
            print("Your health",player_hp)
        else:
            player_hp = Apple + Max_hp
            print("Your health",player_hp)
if inventory_bread > 0:
   if which_eat.capitalize() == "Bread":
      if Bread + player_hp > Max_hp:
            player_hp = Max_hp
            print("Your health",player_hp)
      else:
           player_hp = Bread + Max_hp
           print("Your health",player_hp)
if inventory_pie > 0:
   if which_eat.capitalize() == "Pie":
      if Pie + player_hp > Max_hp:
            player_hp = Max_hp
            print("Your health",player_hp)
      else:
            player_hp = Pie + Max_hp
            print("Your health",player_hp)