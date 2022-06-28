list_of_strings = ['2', '0', '8', '3']


def string_to_int(list_of_strings=[]):
    list_of_number = []
    for value in list_of_strings:
        list_of_number.append(int(value))
    return list_of_number


def to_filter_range(list_of_int=[], range_for_filter=int):
    list_after_filter = []
    list_of_int.sort()
    for index in range(range_for_filter - 1, list_of_int.__len__()):
        list_after_filter.append(list_of_int[index])
    return list_after_filter


print(to_filter_range(string_to_int(list_of_strings), 3))
