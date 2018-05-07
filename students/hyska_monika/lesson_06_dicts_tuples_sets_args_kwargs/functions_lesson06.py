import random


# function draws n numbers for set range
def list_random(n, range_min, range_max):
    # my_list = [int(randint(range_min, range_max)) for i in range(n)]
    my_list = random.sample(range(range_min, range_max), n)
    print(' '.join(map(str, my_list)))
    return my_list


# function to create dictionary with n elements and print (put key and value from keyboard)
def create_inventory():
    n = int((input("Number of dictionary elements:")))
    inventory = {}
    for i in range(n):
        inventory.setdefault((int(input("Key:"))),(int(input("Value:"))))
    print("Inventory:", inventory)
    return inventory


# function display dictionary, first value, next key
def display_inventory(inventory):
    print("Inventory:")
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
        asked_numbers.setdefault(i + 1, 1)
    return asked_numbers


# function search max value in dictionary and return key for this max
def find_max(dict):
    max_key = [key for key, val in dict.items() if val == max(dict.values())]
    print(' '.join(map(str, max_key)))
    return max_key


# function change list to dictionary. For key set first element for value set list with next elements
# eg. return {'kot.j' : ['r', 'w',  'x'], 'pies.l' : ['r'], 'mysz' : ['r', 'x']}
def change_to_dict(mylist):
    inventory = {}
    for i in range(len(mylist)):
        i_elem = mylist[i]
        split_elements = i_elem.split(' ')
        key_elem = split_elements[0]
        del split_elements[0]
        values_elem = split_elements
        inventory.setdefault(key_elem, values_elem)
    return inventory


# function open file with rights to reading
def file_to_list(file_name):
    my_file = open(file_name, "r")
    words_list = my_file.read().split()
    return words_list
