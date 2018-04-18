def lista_int(list):
    list_int = []
    for i in list:
        list_int.append(int(i))
    return list_int


def grearer_than_neighbours(list):
    greaters = 0
    for i in range(1, len(list) - 1):
        if list[i] > list[i - 1]:
            if list[i] > list[i + 1]:
                greaters += 1

    return greaters


l = input()
list = l.split(" ")
print(grearer_than_neighbours(lista_int(list)))
