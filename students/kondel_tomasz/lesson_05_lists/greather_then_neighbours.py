str_list = '-9 29 -100 64 26 73 -96 28 -92 11 -14 -86 -54 -67'


def greater_then_neighbours(input_string):
    # convert string to list
    val_list = []
    splitted_string = input_string.split(' ')
    for item in splitted_string:
        val_list.append(int(item))

    # check length of list
    list_len = len(val_list)
    if list_len <= 2:
        return 0

    # compare
    cnt = 0
    for idx in range(1, list_len - 1):
        if val_list[idx] > val_list[idx - 1] and \
           val_list[idx] > val_list[idx + 1]:
            cnt += 1
    return cnt


x = greater_then_neighbours(str_list)
print(x)
