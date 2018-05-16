# https://automatetheboringstuff.com/chapter5/
# List to Dictionary Function for Fantasy Game Inventory
# piotrsta

from fantasy_game_inventory import display_inventory


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)
            inventory[item] += 1
    return inventory


if __name__ == "__main__":
    inv = {'gold coin': 42, 'rope': 1}
    display_inventory(inv)

    print('You found the dragon loot!')
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
