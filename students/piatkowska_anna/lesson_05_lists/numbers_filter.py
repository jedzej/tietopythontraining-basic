'''
Numbers filter - using list comprehensions write a function that
casts list of strings to list of integers and filters numbers within
supplied range. Example data:
list_of_strings = ['1', '2', '0', '8', '3']
to_filter_range = range(3)
expected_output = [8, 3]
'''


def filter(list, range):
    output = []
    for elem in list:
        for f in range:
            if (int(elem) == f):
                break
        else:
            output.append(int(elem))
    print(output)


if __name__ == "__main__":
    try:
        list_of_strings = ['1', '2', '0', '8', '3']
        to_filter_range = range(3)
        filter(list_of_strings, to_filter_range)
    except ValueError:
        print("Invalid params")
