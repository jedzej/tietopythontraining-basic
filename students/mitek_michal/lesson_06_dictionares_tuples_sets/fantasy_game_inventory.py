
def display_inventory(inventory):

        print("Inventory: ")
        item_total = 0

        for k, v in inventory.items():
            item_total = item_total + v
            print(str(inventory.get(k, 0)) + ' ' + k)

        print("Total number of items " + str(item_total))


def add_to_inventory(inventory, added_items):

    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
