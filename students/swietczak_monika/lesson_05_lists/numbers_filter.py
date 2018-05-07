# list_of_strings = ['1', '2', '8', '3', '0', '9']
list_of_strings = input(
    "Enter a list of numbers, each number "
    "should be followed by comma: ").split(",")


def convert_to_ints(lista):
    """
    Converts given list of strings into list of integers, if a value is not
    string, ValueError is catch
    :param lista: list of strings
    :return: converted list of integers
    """
    list_of_ints = []
    for val in lista:
        try:
            list_of_ints.append(int(val))
        except ValueError:
            print("Incorrect type")
    return list_of_ints


def to_filter_range(n, str_list):
    """
    Filters values within given range
    :param n: value to filter
    :param str_list: list of strings
    :return: list of integers with values less than n
    """
    int_list = convert_to_ints(str_list)
    result_list = [val for val in int_list if val < n]
    '''for val in int_list:
        if val < n:
            result_list.append(val)'''
    return result_list


print(to_filter_range(3, list_of_strings))
