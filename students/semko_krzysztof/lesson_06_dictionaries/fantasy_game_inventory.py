"""
You are creating a fantasy video game. The data structure
 to model the player’s inventory will be a dictionary
 where the keys are string values describing the item in
 the inventory and the value is an integer value detailing
 how many of that item the player has. For example, the
 dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42,
 'dagger': 1, 'arrow': 12} means the player has 1 rope,
 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take
any possible “inventory” and display it like the following:
"""


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + " " + str(key))
        item_total += value
    print("Total number of items: " + str(item_total))


def main():
    display_inventory(stuff)


if __name__ == '__main__':
    main()
