# Function return/print list when element is in range
from create_lists import list_elements_str
from create_lists import list_to_int


def rangelist(mylist):
    filter_range = int((input("Range: ")))
    new_list = [mylist[x] for x in range(len(mylist))
                if mylist[x] >= filter_range]
    print("New List:", new_list)
    return new_list


rangelist(list_to_int(list_elements_str()))
