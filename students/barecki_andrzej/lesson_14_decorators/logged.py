# Write @logged decorator using logger_wrapper from lesson 6. Apply it to
#  several functions to demonstrate that it works.


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    return foo(*args, **kwargs)


def inspect_args(*args, **kwargs):
    item = 0
    for elem in args:
        print("  args param {0} is equal: {1}".format(item, str(elem)))
        item += 1
    for key, value in kwargs.items():
        print("kwargs param {0} is equal: {1}".format(key, str(value)))


def logged(func):
    def func_wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def func_1(a, b, c, d, e):
    print("{0}, {1}, {2}, {3}, {4}".format(a, b, c, d, e))


@logged
def func_2(my_str):
    print("String: >>>{0}<<< length is equal: {1}"
          .format(my_str, len(my_str)))


@logged
def func_3(a, b):
    return a + b


def main():
    func_1(1, 2, 3, d='4', e='5')
    func_2("Ala ma kota")
    print("Result of sum: {0}".format(str(func_3(4, 6))))


if __name__ == '__main__':
    main()
