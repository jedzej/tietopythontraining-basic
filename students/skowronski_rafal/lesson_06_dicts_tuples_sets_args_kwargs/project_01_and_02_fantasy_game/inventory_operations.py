import copy
from inventory import display_inventory


def add_to_inventory(inventory, added_items):
    inv = copy.deepcopy(inventory)
    for item in added_items:
        count = inv.get(item, 0) + 1
        inv[item] = count

    return inv


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
