from fantasy_game_inventory import display_inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


if __name__ == '__main__':
    main()
