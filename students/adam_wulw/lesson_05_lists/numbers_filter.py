list_of_strings = ['2', '0', '8', '3']
to_filter_range = range(3)


def my_filter(data, filter_range):
    data = list(map(int, data))
    output = []
    filter_match = 0
    for item in data:
        for filter_item in filter_range:
            if filter_item == item:
                filter_match = 1
        if not filter_match:
            output.append(item)
        filter_match = 0
    return output


print(my_filter(list_of_strings, to_filter_range))
