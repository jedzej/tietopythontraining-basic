#!/usr/bin/env python3

"""
args_and_kwargs.py: practice projects related to *args and **kwargs:
"Args sum", "Args inspector" and "Logger wrapper" from:
Lesson 6 - Dictionaries, tuples and sets + *args and **kwargs
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def sum_all(*args):

    args_sum = 0

    for num in args:
        args_sum += num

    return args_sum


def inspect_args(*args, **kwargs):

    num = 0

    print('args:')
    for arg in args:
        print("arg_{}: {}".format(num, arg), end=', ')
        num += 1

    print('\nkwargs:')
    for name, value in kwargs.items():
        print("{}: {}".format(name, value), end=', ')

    print(' ')


def logger_wrapper(foo, *args, **kwargs):

    print("Called function: " + foo.__name__)
    inspect_args(*args, **kwargs)
    return foo(*args, **kwargs)


def dummy_fun(dummy_tuple, dummy_dict, dummy_float, dummy_str='default_str'):

    del dummy_tuple, dummy_dict, dummy_float, dummy_str
    return None


def main():

    # Args sum
    print(sum_all(1, 2, -5, 2.0, 11.56, 10))
    print('')

    # Args inspector
    inspect_args(1, [125, 2.0, 'qwerty'], name='Daniel', x=5)
    print('')

    # Logger wrapper
    received_sum = logger_wrapper(sum_all, 1, 2, -3, 4, 5)
    print("received_sum = {}\n".format(received_sum))
    logger_wrapper(dummy_fun, (1, 2, 'ABC'), dummy_float=125.81,
                   dummy_str='abc', dummy_dict={"abc": 5, "defg": 4})


if __name__ == '__main__':
    main()
