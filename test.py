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
gold = (100)
from shop import shop
choice = input("What do you want to do?: shop/inventory: ").capitalize
if choice == "Shop":
    shop()
else:
    print("L")
