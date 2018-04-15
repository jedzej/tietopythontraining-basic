# Function return/print number of elements that are greater than both of their neighbors
from create_lists import list_elements


def greater_than_neighbours(mylist):
    count = 0
    for i in range(1, len(mylist) - 1):
        if mylist[i - 1] < mylist[i] > mylist[i + 1]:
            count += 1
    print('Greater Than Neighbours:', count)


greater_than_neighbours(list_elements())
