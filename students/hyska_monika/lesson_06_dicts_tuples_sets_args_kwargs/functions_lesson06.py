import random


# function draws n numbers for set range
def list_random(n, range_min, range_max):
    # my_list = [int(randint(range_min, range_max)) for i in range(n)]
    my_list = random.sample(range(range_min, range_max), n)
    print(' '.join(map(str, my_list)))
    return my_list


# function to create dictionary
# with n elements and print (put key and value from keyboard)
def create_inventory():
    n = int((input("Number of dictionary elements: ")))
    inventory = {}
    for i in range(n):
        inventory.update({int(input("Key: ")): int(input("Value: "))})
    print("Inventory: ", inventory)


# function display dictionary, first value, next key
def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += inventory[k]
    print("\nTotal number of items: " + str(item_total))


# function to create list with n elements
def list_elements_str():
    n = int((input("Size of list:")))
    mylist = []
    for i in range(n):
        i = str((input("put element:")))
        mylist.append(i)
    return mylist


# function crete dictionary with key 1,2,..,n and value = 1
def create_dict_to_n(n):
    asked_numbers = {}
    for i in range(n):
        asked_numbers[i + 1] = 1
    return asked_numbers


# function search max value in dictionary and return keys for this max
def find_max(dict):
    max_value = max(dict.values())
    max_key = [key for key, val in dict.items() if val == max_value]
    print(' '.join(map(str, max_key)))
    return max_key


# function change list to dictionary.
# For key set first element for value set list with next elements
# eg. return
# {'kot.j' : ['r', 'w',  x'], 'pies.l' : ['r'], 'mysz' : ['r', 'x']}
def change_to_dict(mylist):
    inventory = {}
    for i in range(len(mylist)):
        i_elem = mylist[i]
        split_elements = i_elem.split(' ')
        key, *values = split_elements
        # -------
        # doesn't work, when put the same key
        # inventory.setdefault(key_elem, values_elem)
        # data wouldn't be save
        # -------
        # when put the same key, data are overwritten
        inventory.update({key: values})
        # inventory[key] = values    # work the same way as update
    return inventory


# function open file with rights to reading
def file_to_list(file_name):
    my_file = open(file_name, "r")
    words_list = my_file.read().split()
    return words_list


# function change dictionary {'Poland' : ['Warsaw', 'Krakow']}
# to dictionary  {'Warsaw': 'Poland, 'Krakow': 'Poland'}
def change_dict_without_list(inventory):
    changed_dict = {}
    for key, values in inventory.items():
        for value in values:
            changed_dict[value] = key
    return changed_dict
