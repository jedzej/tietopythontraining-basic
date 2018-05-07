def display_inventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += int(v)

    print('Total number of items: ' + str(item_total))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)
