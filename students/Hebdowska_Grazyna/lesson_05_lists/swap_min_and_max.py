def lista_int(list):
    list_int = []
    for i in list:
        list_int.append(int(i))
    return list_int


def swap_min_and_max(list):
    i_max = 0
    max_value = list[0]
    i_min = 0
    min_value = list[0]
    for i in range(1, len(list)):
        if max_value < list[i]:
            max_value = list[i]
            i_max = i

        if min_value > list[i]:
            min_value = list[i]
            i_min = i

    list[i_min] = max_value
    list[i_max] = min_value

    return list


l = input()
list = lista_int(l.split(" "))
print(swap_min_and_max(list))
