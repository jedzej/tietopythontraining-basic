""" Projects: 6, 7 & 8 """


def sum_all(*args):
    return sum(args)


def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, val in kwargs.items():
        print("{}: {}".format(key, val))


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def my_foo(*args, **kwargs):
    print("Calling my_foo with:\n args: {}\n kwargs: {}".format(args, kwargs))


if __name__ == '__main__':
    print(sum_all(1, 5, 32))
    logger_wrapper(my_foo, 55, second=2, third='a')
