def main():
    any_function(1, 2, 3, d='4', e='5')
    logger_wrapper(any_function, 1, 2, 3, d='4', e='5')


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def inspect_args(*args, **kwargs):
    item = 0
    for elem in args:
        print("  args param {0} is equal {1}".format(item, str(elem)))
        item += 1
    for key, value in kwargs.items():
        print("kwargs param {0} is equal {1}".format(key, str(value)))


def any_function(a, b, c, d, e):
    print("{0}, {1}, {2}, {3}, {4}".format(a, b, c, d, e))


if __name__ == '__main__':
    main()
