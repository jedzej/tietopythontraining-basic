stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
    print("Total number of items: " + str(sum(inventory.values())))

displayInventory(stuff)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
displayInventory(inv)