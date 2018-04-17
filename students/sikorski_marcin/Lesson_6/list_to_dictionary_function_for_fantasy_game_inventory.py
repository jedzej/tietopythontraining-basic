stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + str(key))
        item_total += value
    print("Total number of items: " + str(item_total))

display_inventory(stuff)


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i], 0)
        inventory[added_items[i]] = inventory[added_items[i]] + 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)
