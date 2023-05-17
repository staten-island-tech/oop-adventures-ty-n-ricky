inventory_apple = 1
inventory_bread = 1
inventory_pie = 1
Max_energy = 100
player_energy = 100
Apple = 20
Bread = 50
Pie = 100
which_eat = input("What food do you want ot eat? (Apple, Bread, Pie) ")
while inventory_apple > 0:
    if which_eat.capitalize == "Apple":
        if Apple + player_energy > Max_energy:
            player_energy = Max_energy
            print(player_energy)
        else:
            player_energy = Apple + Max_energy
            print(player_energy)
while inventory_bread > 0:
   if which_eat.capitalize == "Bread":
      if Bread + player_energy > Max_energy:
            player_energy = Max_energy
            print(player_energy)
      else:
           player_energy = Bread + Max_energy
           print(player_energy)
while inventory_pie > 0:
   if which_eat.capitalize == "Pie":
      if Pie + player_energy > Max_energy:
            player_energy = Max_energy
            print(player_energy)
      else:
            player_energy = Pie + Max_energy
            print(player_energy)