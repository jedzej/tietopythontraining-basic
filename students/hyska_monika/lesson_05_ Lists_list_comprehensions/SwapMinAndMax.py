# Funcion swap the minimal and maximal elements list
from create_lists import list_elements


def swap_min_max(mylist):
    minimum = min(mylist)
    maximum = max(mylist)
    min_index = mylist.index(minimum)
    max_index = mylist.index(maximum)
    mylist[min_index] = maximum
    mylist[max_index] = minimum
    print("List after swap min and max: ", mylist)


swap_min_max(list_elements())
