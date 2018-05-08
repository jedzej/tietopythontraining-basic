from fantasy_game_inventory import displayInventory


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1
    return inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)


if __name__ == '__main__':
    main()
