""" Projects: 1 & 2 """


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
