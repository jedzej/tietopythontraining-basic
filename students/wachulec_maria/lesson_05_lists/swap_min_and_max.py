def swap_min_and_max():
    primary_list = [int(s) for s in input().split()]
    result_list = primary_list.copy()
    result_list[primary_list.index(max(primary_list))] = min(primary_list)
    result_list[primary_list.index(min(primary_list))] = max(primary_list)
    return result_list


r = swap_min_and_max()
print(' '.join([str(i) for i in r]))
