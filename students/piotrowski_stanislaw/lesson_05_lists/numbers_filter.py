# piotrsta
# Numbers filter
# Using list comprehensions write a function that casts list of strings
# to list of integers and filters numbers within supplied range.

# Example data:
# list_of_strings = ['2', '0', '8', '3']
# to_filter_range = range(3)
# expected_output = [8, 3]


def numbers_filter(input_list, input_range):
    output_list = [int(x) for x in input_list if int(x) not in input_range]
    return output_list


if __name__ == '__main__':
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)

    print(numbers_filter(list_of_strings, to_filter_range))
