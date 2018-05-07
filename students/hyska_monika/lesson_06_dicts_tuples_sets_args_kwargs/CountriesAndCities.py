# Function print country name for city
from functions_lesson06 import list_elements_str, change_to_dict


def countries_and_cities(inventory):
    n = int((input("How cities do you want check?: ")))
    for i in range(n):
        city = str((input("put city:")))
        country = None
        for k, v in inventory.items():
            if city in inventory[k]:
                country = k
                break
        if country is None:
            print("Missing city on list.")
        else:
            print("country: ", country)


print("For one element of list put country and cities, separate using space."
      "\nEg. Poland Warsszawa Wroclawa Krakow")
countries_and_cities(change_to_dict(list_elements_str()))
"""
inventory = {'USA' : ['Dallas', 'Chicago',  'Atlanta'],
             'Polska' : ['Warszawa', 'Krakow'],
             'Niemcy' : ['Berlin', 'Dresno']}
countries_and_cities(inventory)
"""
