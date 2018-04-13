#!/usr/bin/env python3


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)


if __name__ == "__main__":
    main()
