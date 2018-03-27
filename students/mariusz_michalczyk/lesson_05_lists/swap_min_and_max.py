def get_index_of_max(list_of_nrs):
    max_nr = max(list_of_nrs)
    return list_of_nrs.index(max_nr)


def get_index_of_min(list_of_nrs):
    min_nr = min(list_of_nrs)
    return list_of_nrs.index(min_nr)


if __name__ == '__main__':
    list_of_nrs = [int(s) for s in input().split()]
    max_index = get_index_of_max(list_of_nrs)
    min_index = get_index_of_min(list_of_nrs)
    list_of_nrs[max_index], list_of_nrs[min_index] = list_of_nrs[min_index], list_of_nrs[max_index]
    print(' '.join([str(item) for item in list_of_nrs]))
