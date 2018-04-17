#!/usr/bin/env python3

"""
fantasy_game.py: a practice projects: "Fantasy Game Inventory"  and "List
to Dictionary Function for Fantasy Game Inventory" from:
https://automatetheboringstuff.com/chapter5/
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def display_inventory(inventory):
    """
    This function  takes a dictionary with inventory and prints it content
    in a nice form
    :param inventory: dictionary of pairs: (string, integer)
    :returns: None
    """
    print("Inventory:")

    item_total = 0

    for k, v in inventory.items():
        item_total += v
        print('{} {}'.format(v, k))

    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    """
    :param inventory: a dictionary representing the player’s inventory
    :param added_items: a list of strings with items to be added to inventory
    :return: dictionary, the updated inventory
    """
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    projects = ['Fantasy Game Inventory',
                'List to Dictionary Function for Fantasy Game Inventory']

    print("{}:\n{}".format(projects[0], len(projects[0]) * '-'))
    display_inventory(stuff)

    print("\n{}:\n{}".format(projects[1], len(projects[1]) * '-'))
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


if __name__ == '__main__':
    main()
