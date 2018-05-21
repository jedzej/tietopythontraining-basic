def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print("{0} - {1}".format(k, v))
        item_total += v
    print("Total number of items: " + str(item_total))


def main():
    print("Result:")
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)


if __name__ == '__main__':
    main()
