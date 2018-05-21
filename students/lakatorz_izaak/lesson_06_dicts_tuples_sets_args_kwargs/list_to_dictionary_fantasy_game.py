# Write a function named addToInventory(inventory, addedItems), where the
# inventory parameter is a dictionary representing the player’s inventory (
# like in the previous project) and the addedItems parameter is a list like
# dragonLoot.
from lesson_06_dicts_tuples_sets_args_kwargs import fantasy_game_inventory


def add_to_inventory(inventory, added_items):
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] = inventory[loot] + 1
    return inventory


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    fantasy_game_inventory.display_inventory(inv)


if __name__ == "__main__":
    main()
