strs = ['2', '0', '8', '3']


def filter_nrs(strs, range_to_filter):
    return [i for i in strs[range_to_filter - 1:len(strs)]]


print(filter_nrs(strs, 3))
