list_of_strings = ['2', '0', '8', '3']


def filter_nrs(list_of_strings, range_to_filter):
    return [i for i in list_of_strings[range_to_filter - 1:len(list_of_strings)]]


print(filter_nrs(list_of_strings, 3))
