stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + str(key))
    print("Total number of items: " + str(item_total))


displayInventory(stuff)


#List to Dictionary Function for Fantasy Game Inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            num_of_items = inventory.get(item)
            inventory[item] = num_of_items + 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
