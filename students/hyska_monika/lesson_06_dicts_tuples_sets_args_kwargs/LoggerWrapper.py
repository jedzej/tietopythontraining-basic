# Function called logger_wrapper that wraps call to
# any function in order to log passed args. The function must take foo,
# *args and **kwargs, prints *args and **kwargs in human readable
# format and finally call foo with args and kwargs


def sum_func(a, b):
    return a + b


def logger_wrapper(foo, *args, **kwargs):
    print('Function return: ', foo)
    print('Arguments:', ', '.join(map(str, args)))
    print('Keyword :')
    for k, v in kwargs.items():
        print(k, "=", v)


my_dict = {'o': '8', 'p': 9}
logger_wrapper(sum_func(3, 9), 5, 7, 8, **my_dict, n=9)
