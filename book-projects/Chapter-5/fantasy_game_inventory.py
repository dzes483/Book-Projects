#!/usr/bin/python3
# fantasy_game_inventory.py - Takes in a dictionary (inventory) and displays it
# in an easy-to-read format. Can also add items to a user's inventory, given an
# additional dictionary object.

INVENTORY = {'rope': 1, 'torch': 6, 'gold coin': 594, 'dagger': 1, 'arrow': 12}
LOOT = ['gold coin', 'dagger', 'gold coin', 'ruby']


def display_inventory(inventory):
    """
    Displays the user's inventory in a nice format, as well as the total number
    of items.
    """
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, loot):
    """
    Given a list, adds the objects to the user's inventory.
    """
    for i in range(len(loot)):
        inventory.setdefault(loot[i], 0)
        inventory[loot[i]] += 1
    return inventory

display_inventory(INVENTORY)
add_to_inventory(INVENTORY, LOOT)
display_inventory(INVENTORY)
