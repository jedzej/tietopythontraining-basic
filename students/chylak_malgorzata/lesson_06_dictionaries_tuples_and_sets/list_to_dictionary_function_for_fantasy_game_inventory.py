from fantasy_game_inventory import display_inventory


def add_to_inventory(inventory, added_items):
    for v in added_items:
        if v in inventory:
            inventory[v] += 1

        else:
            inventory[v] = 1

    return inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)

    display_inventory(inv)


if __name__ == "__main__":
    main()
