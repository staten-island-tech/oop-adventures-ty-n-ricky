which_map = input("Where do you want to travel? (Shop,Dungeon,Dungeon2) ")
if which_map.capitalize() == "Shop":
  from shop import shop
elif which_map.capitalize() == "Dungeon":
  from dungeon import dungeon
elif which_map.capitalize() == "Dungeon2":
  from dungeon2 import dungeion2
else: 
  print("Please try again 💋")