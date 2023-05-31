def map():
  which_map = input("Where do you want to travel? (Shop,Dungeon,Inventory) ")
  if which_map.capitalize() == "Shop":
    from shop import shop
    shop
  elif which_map.capitalize() == "Dungeon":
    from dungeon import randoms
    randoms
  elif which_map.capitalize() == "Inventory":
    from inventory import inventory
    inventory
  else: 
    print("Please try again 💋")
map()
continues = input("Do you want to continue? Y/N 💋 ")
while continues.capitalize() == "Y":
  map()
  continues = input("Do you want to continue? Y/N 💋 ")