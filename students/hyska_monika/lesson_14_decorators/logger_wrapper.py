"""
Write @logged decorator using logger_wrapper from lesson 6.
Apply it to several functions to demonstrate that it works.
"""


def logged(func):
    def func_wrapper(*args, **kwargs):
        print('Function return: ', func(*args, **kwargs))
        print('Arguments:', ', '.join(map(str, args)))
        print('Keyword :')
        for k, v in kwargs.items():
            print(k, "=", v)
        return func(*args, **kwargs)
    return func_wrapper


@logged
def sum_func(a, b):
    return a + b


@logged
def add_to_list(my_list, *args):
    args_list = list(args)
    my_list_new = my_list + args_list
    return list(my_list_new)


@logged
def add_to_dict(my_dict, **kwargs):
    for k, v in kwargs.items():
        my_dict[k] = v
    return my_dict


sum_func(3, 9)
print()

my_list = [1, 5]
add_to_list(my_list, 8, 5)
print()

my_dict = {'o': '8', 'p': 9}
add_to_dict(my_dict, z=5, k=2)
