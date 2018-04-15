# Function print list in '' and with ",", before last element put "and"
from create_lists import list_elements_str


def coma_code(mylist):
    sent_str = ""
    for elem in range(len(mylist)):
        if elem == 0:
            sent_str += "\'" + mylist[elem] + ", "
        elif elem == len(mylist) - 1:
            sent_str += "and " + mylist[elem] + "\'"
        else:
            sent_str += mylist[elem] + ", "
    print(sent_str)


coma_code(list_elements_str())
