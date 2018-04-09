def filterfunction(strings, scope):
    elements = [int(element) for element in strings if int(element) not in scope]
    return elements


if __name__ == "__main__":

    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    print(filterfunction(list_of_strings, to_filter_range))
