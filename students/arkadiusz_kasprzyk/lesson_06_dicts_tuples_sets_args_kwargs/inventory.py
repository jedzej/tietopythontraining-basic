# inventory.py


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for k in addedItems:
        inventory.setdefault(k, 0)
        inventory[k] += 1


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(stuff)
print()

addToInventory(stuff, dragonLoot)

displayInventory(stuff)
