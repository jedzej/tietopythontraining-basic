# Function print country name for city
from functions_lesson06 import list_elements_str, change_to_dict,\
    change_dict_without_list


# search country if dictionary have lists inside
def countries_and_cities(inventory):
    n = int((input("How many cities do you want to check?: ")))
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


# search country if dictionary doesn't have list inside
def search_country_for_city(inventory):
    n = int((input("How many cities do you want to check?: ")))
    for i in range(n):
        city = str((input("put city:")))
        country = inventory.get(city)
        if country is None:
            print("Missing city on list.")
        else:
            print("country: ", country)


print("For one element of list put country and cities, separate using space."
      "\nEg. Poland Warsszawa Wroclawa Krakow")
countries_and_cities_list = change_to_dict(list_elements_str())
# countries_and_cities(countries_and_cities_list)
search_country_for_city(change_dict_without_list(countries_and_cities_list))
"""
inventory = {'USA' : ['Dallas', 'Chicago',  'Atlanta'],
             'Polska' : ['Warszawa', 'Krakow'],
             'Niemcy' : ['Berlin', 'Dresno']}
search_country_for_city(change_dict_without_list(inventory))
"""
