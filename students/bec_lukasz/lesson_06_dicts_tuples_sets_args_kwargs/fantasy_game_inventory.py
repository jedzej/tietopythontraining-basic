class FantasyGameInventory(object):

    def display_inventory(self, inv):
        print('Inventory: ')
        items = 0
        for i, j in inv.items():
            items += j
            print(i + ' ' + str(j))
        print("Total number of items: " + str(items))

    def add_to_inventory(self, inv, added_items):
        for i in added_items:
            if i in inv.keys():
                inv[i] += 1
            if i not in inv.keys():
                inv.setdefault(i, 1)


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

f = FantasyGameInventory()
f.display_inventory(inventory)
f.add_to_inventory(inventory, dragonLoot)
print()
f.display_inventory(inventory)
