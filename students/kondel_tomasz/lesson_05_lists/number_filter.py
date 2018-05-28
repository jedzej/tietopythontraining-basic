list_of_strings = ['2', '0', '8', '3', '6', '0', '1', '0', '9']
to_filter_range = range(3)
expected_output = [8, 3]


def filters(list_string, list_filter):
    list_of_values = list(int(x) for x in list_string)
    # print(list_of_values)
    val_position = 0
    while val_position < len(list_of_values):
        if list_of_values[val_position] in list_filter:
            list_of_values.remove(list_of_values[val_position])
        else:
            val_position += 1
    return list_of_values


print(filters(list_of_strings, to_filter_range))
