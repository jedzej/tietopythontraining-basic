def display_inventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += int(v)

    print('Total number of items: ' + str(item_total))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
