spam = ['apples', 'bananas', 'tofu', 'cats']


def comma_code(some_list):
    """
    Converts a list to string containing items separated by commas
    :param some_list: list
    :return: string containing converted list
    """
    converted = ""
    for i in range(len(some_list) - 1):
        converted += some_list[i] + ', '
    converted += "and " + some_list[-1]
    return converted


print(comma_code(spam))
