#!/usr/bin/env python3


import pprint


def inspect_args(*args, **kwargs):
    pp = pprint.PrettyPrinter(width=1)
    print("Passed args:")
    pp.pprint(args)

    print("Passed kwargs:")
    pp.pprint(kwargs)


def logger_wrapper(foo, *args, **kwargs):
    print(" {} ".format(foo).center(80, '='))
    inspect_args(*args, **kwargs)
    print("Result of {} operation with above args and kwargs is:".format(foo))
    print(foo(args, **kwargs))


def logged(func):
    def func_wrapper(*args, **kwargs):
        logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def dummy_sort(*args, **kwargs):
    return sorted(*args, **kwargs)


@logged
def dummy_func(*args, **kwargs):
    return None


def main():
    print("\n1)")
    dummy_sort(1, 2, 3, 4, 5, 6, 7, 8, reverse=True)

    print("\n2)")
    dummy_sort(("zbyszek", 3), ("adam", 1), ("wojtek", 2), ("rysiek", 2),
               ("gerwazy", 1), key=lambda x: (-x[1], x[0]))

    print("\n3)")
    dummy_func("These arguments", "doesn't have", "any", "sense", 667, True)


if __name__ == "__main__":
    main()
