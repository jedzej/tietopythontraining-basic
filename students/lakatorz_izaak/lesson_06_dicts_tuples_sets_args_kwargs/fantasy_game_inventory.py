# Write a function named displayInventory() that would take any possible
# “inventory” and display it like the following:

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k, sep=' ')
        item_total += v
    print("Total number of items: " + str(item_total))


def main():
    display_inventory(stuff)


if __name__ == "__main__":
    main()
