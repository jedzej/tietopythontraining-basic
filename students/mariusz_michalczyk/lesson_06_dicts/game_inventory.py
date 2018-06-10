inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'ruby',
              'gold coin',
              'ruby']


def add_to_inventory(inv, items):
    for item in items:
        if item in inv.keys():
            inv[item] += 1
        else:
            inv[item] = 1
    return inv


def display_inventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(str(k) + " " + str(v))
        item_total += v
    print("Total number of items: " + str(item_total))


if __name__ == '__main__':
    updated_inv = add_to_inventory(inv, dragonLoot)
    display_inventory(updated_inv)
