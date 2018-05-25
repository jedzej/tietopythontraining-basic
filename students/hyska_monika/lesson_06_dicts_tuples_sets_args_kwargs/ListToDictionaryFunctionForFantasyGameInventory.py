# function to add items to dictionary
from FantasyGameInventory import display_inventory
# dlaczego podczas importu wykonuje mi linnie 13 i 14
# z FantasyGameInventory?


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
        """
        # my first way
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
        """
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
