from random import randint


# create list with n put elements(int)
def list_elements():
    n = int((input("How many elements does the list have?: ")))
    mylist = []
    for i in range(n):
        i = int((input("put element: ")))
        mylist.append(i)
    print("List:", mylist)
    return mylist


# create list with n put elements(str)
def list_elements_str():
    n = int((input("Size of list: ")))
    mylist = []
    for i in range(n):
        i = str((input("put element: ")))
        mylist.append(i)
    print("List:", mylist)
    return mylist


# create dimensional lists(array) with n random elements
def array_2dem_random():
    n = int((input("How many rows?: ")))
    m = int((input("How many columns?: ")))
    mylist = [[int(randint(-100, 100)) for j in range(m)] for i in range(n)]
    for row in mylist:
        print(' '.join([str(elem) for elem in row]))
    return mylist


# create dimensional lists(array) with n put elements
def array_2dem_put():
    n = int((input("How many rows?: ")))
    m = int((input("How many columns?: ")))
    mylist = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        print("Put element for", i, "row")
        for j in range(m):
            mylist[i][j] = int((input()))
    for row in mylist:
        print(' '.join([str(elem) for elem in row]))
    return mylist


# convert (on list) strings elements to integer
def list_to_int(mylist):
    mylist = list(map(int, mylist))
    print("Converted list: ", mylist)
    return mylist
