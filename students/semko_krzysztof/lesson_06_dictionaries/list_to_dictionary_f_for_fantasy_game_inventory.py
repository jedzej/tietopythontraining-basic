"""
Imagine that a vanquished dragon’s loot is represented
as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin',
'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems),
where the inventory parameter is a dictionary representing
the player’s inventory (like in the previous project) and
the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that
represents the updated inventory. Note that the addedItems
list can contain multiples of the same item.
Your code could look something like this:
"""
from fantasy_game_inventory import display_inventory


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        if inventory.get(item):
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


if __name__ == '__main__':
    main()
