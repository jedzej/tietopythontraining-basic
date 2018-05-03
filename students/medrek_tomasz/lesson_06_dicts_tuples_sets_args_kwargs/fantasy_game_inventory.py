#!/usr/bin/env python3


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inv, added_items):
    for item in added_items:
        inv.setdefault(item, 0)
        inv[item] += 1


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


if __name__ == "__main__":
    main()
