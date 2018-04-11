spam = ['apples', 'bananas', 'tofu', 'cats']


def get_comma_string(my_list):
    my_list[-1] = "and " + my_list[-1]
    return ', '.join(my_list)


print(get_comma_string(spam))
