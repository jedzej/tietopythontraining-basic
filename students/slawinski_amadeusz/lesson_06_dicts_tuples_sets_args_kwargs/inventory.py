#!/usr/bin/env python3


def displayInventory(inventory):
    print("Inventory:")
    if inventory is None:
        print("No items - go hunt some dragons!")
    else:
        item_count = 0
        for k, v in inventory.items():
            print("{} {}".format(v, k))
            item_count += v
        print("Total number of items: {}".format(item_count))


def addToInventory(inventory, addedItems):
    if inventory is None:
        inventory = {}
    if addedItems is not None:
        for item in addedItems:
            inventory.setdefault(item, 0)
            inventory[item] += 1
    return inventory


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

inv = addToInventory(inv, None)
displayInventory(inv)

inv = addToInventory(None, {'necronomicon': 1})
displayInventory(inv)

displayInventory(None)
