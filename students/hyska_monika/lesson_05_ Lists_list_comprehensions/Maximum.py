# Function print maximum index for array
from create_lists import array_2dem_random
# from create_lists import array_2dem_put


def max_index(mylist):
    # maximum = max([max(i) for i in mylist])
    # if I use it, how I can find index?
    maximum = mylist[0][0]
    index = [0, 0]
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            if mylist[i][j] > maximum:
                maximum = mylist[i][j]
                index = [i, j]
    print("index for max is:", index)


max_index(array_2dem_random())
# max_index(array_2dem_put)
