def number_filter(n, filter_range):
    return [int(i) for i in n if int(i) not in range(filter_range)]


list_of_strings = ['2', '0', '8', '3']
filter_range = 3

print(number_filter(list_of_strings, filter_range))