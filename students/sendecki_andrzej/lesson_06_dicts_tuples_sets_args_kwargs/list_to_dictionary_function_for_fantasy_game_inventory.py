def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        default_value = inventory.get(item, 0)
        if item in inventory:
            inventory[item] = default_value + 1
        else:
            inventory.setdefault(item, default_value + 1)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
