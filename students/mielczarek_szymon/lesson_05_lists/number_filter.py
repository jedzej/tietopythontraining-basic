
def filter_numbers(list_of_strings, filter_range):
    return [int(i) for i in list_of_strings if int(i) not in filter_range]


if __name__ == "__main__":
    list_of_strings = ['1', '2', '0', '8', '3']
    to_filter_range = range(3)
    print(filter_numbers(list_of_strings, list(to_filter_range)))
    # expected_output = [8, 3]
