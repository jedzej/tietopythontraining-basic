def numbers_filter(base_list, filter_range):
    numeric_list = [int(i) for i in base_list
                    if int(i) not in list(filter_range)]
    return numeric_list


list_of_strings = input().split()
to_filter_range = range(3)
print(numbers_filter(list_of_strings, to_filter_range))
