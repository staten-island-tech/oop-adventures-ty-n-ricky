which_map = input("Where do you want to travel? (Shop,Dungeon) ")
if which_map.capitalize() == "Shop":
  from shop import shop
elif which_map.capitalize() == "Dungeon":
  from dungeon import randoms
elif which_map.capitalize() == "Inventory":
  from inventory import inventory
else:
  print("Please try again 💋")

