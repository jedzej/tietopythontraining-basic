stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + str(key))
        item_total += value
    print("Total number of items: " + str(item_total))

display_inventory(stuff)
