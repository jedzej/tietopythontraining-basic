list_of_strings = ['2', '0', '8', '3', '11', '22']
range = 10


def filter_ints(integers, filter_range):
    return [int(x) for x in integers if int(x) >= filter_range]


print(filter_ints(list_of_strings, range))
