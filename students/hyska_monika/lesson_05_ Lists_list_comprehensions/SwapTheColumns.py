# Function return/print array after swap columns
from create_lists import array_2dem_random


def swap_columns(mylist):
    i = int((input("First column to swap: ")))
    j = int((input("Second column to swap: ")))
    for elem in range(len(mylist)):
        temp = mylist[elem][i]
        mylist[elem][i] = mylist[elem][j]
        mylist[elem][j] = temp
    for row in mylist:
        print('   '.join([str(elem) for elem in row]))
    return mylist


swap_columns(array_2dem_random())
