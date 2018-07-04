stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory, new_inventory):
    for i in range(len(new_inventory)):
        if new_inventory[i] in inventory.keys():
            inventory[new_inventory[i]] += 1
        else:
            inventory[new_inventory[i]] = 1
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k, '=', v)
        item_total += v
    print("Total number of items: " + str(item_total))


def added_to_inventory():
    items_to_add = []
    while True:
        a = str(input('give a name of new item( 1 - for quit ): '))
        if a == '1':
            break
        items_to_add.append(a)
    return items_to_add


added_inventory = added_to_inventory()
added_to_inventory()
display_inventory(stuff, added_inventory)
