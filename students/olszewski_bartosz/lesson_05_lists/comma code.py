def list_elements_collecting():
    list_of_names = []
    while True:
        a = str(input())
        if a == "q":
            break
        list_of_names.append(str(a))
    return list_of_names


def printing(b):
    list_range = len(b)
    for a in range(list_range - 2):
        print(b[a], end=", ")
    print(b[-2], end=" ")
    print("and ", end="")
    print(b[-1])


name_list = list_elements_collecting()
list_elements_collecting()
printing(name_list)
