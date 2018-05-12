list_of_strings = [str(x) for x in input().split()]
to_filter_range = range(int(input()))
filtered_list_of_ints = [int(x) for x in list_of_strings
                         if int(x) not in to_filter_range]
print(filtered_list_of_ints)
