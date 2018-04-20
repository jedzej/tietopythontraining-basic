def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, " ", k)
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        print(item)
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42,
                 'dagger': 1, 'arrow': 12}
    display_inventory(inventory)
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    display_inventory(inv)
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


if __name__ == "__main__":
    main()
