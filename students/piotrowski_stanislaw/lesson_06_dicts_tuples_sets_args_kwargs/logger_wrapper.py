# http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec231
# Logger wrapper - write a function called logger_wrapper that wraps call to any function in order to log passed args.
#     The function must take foo, *args and **kwargs, prints *args and **kwargs in human readable format and finally
#     call foo with args and kwargs
# piotrsta

from args_inspector import inspect_args


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(args, kwargs)


def some_function(*args, **kwargs):
    print('This is an example of a function.')


if __name__ == "__main__":
    logger_wrapper(some_function, 1, 2.0, third='3')
