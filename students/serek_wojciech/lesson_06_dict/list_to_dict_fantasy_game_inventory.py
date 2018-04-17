#!/usr/bin/env python3
"""List to Dictionary Function for Fantasy Game Inventory exercise"""
from fantasy_game_inventory import display_inventory


def add_to_inventory(inventory, added_items):
    """Add items to inventory"""
    for item in added_items:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1
    return inventory


def main():
    """Main function"""
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    print('Inventory before update:')
    display_inventory(inv)

    inv = add_to_inventory(inv, dragon_loot)

    print('Inventory after update:')
    display_inventory(inv)


if __name__ == '__main__':
    main()
