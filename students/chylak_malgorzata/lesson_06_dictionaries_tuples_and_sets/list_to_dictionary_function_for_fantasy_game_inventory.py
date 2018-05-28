from fantasy_game_inventory import display_inventory


def addToInventory(inventory, addedItems):
    for v in addedItems:
        if v in inventory:
            inventory[v] += 1

        else:
            inventory[v] = 1

    return inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragon_loot)

    display_inventory(inv)


if __name__ == "__main__":
    main()
