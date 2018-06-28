def swap_min_max(list):
    min = list[0]
    max = list[0]
    min_place = 0
    max_place = 0
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
            max_place = i
        if list[i] < min:
            min = list[i]
            min_place = i
    list[min_place] = max
    list[max_place] = min
    return list


test_list = [-33, 4, 59999999999, 2, 4444]
print(swap_min_max(test_list))
