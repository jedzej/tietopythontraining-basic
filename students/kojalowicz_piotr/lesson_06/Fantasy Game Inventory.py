stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
    print("Total number of items: " + str(sum(inventory.values())))


display_inventory(stuff)
