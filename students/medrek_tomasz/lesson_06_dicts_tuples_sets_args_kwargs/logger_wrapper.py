#!/usr/bin/env python3


from args_inspector import inspect_args


def logger_wrapper(foo, *args, **kwargs):
    print(" {} ".format(foo).center(80, '='))
    inspect_args(*args, **kwargs)
    print("Result of {} operation with above args and kwargs is:".format(foo))
    print(foo(args, **kwargs))


def main():
    logger_wrapper(sorted, 1, 2, 3, 4, 5, 6, 7, 8, reverse=True)
    logger_wrapper(sorted, ("zbyszek", 3), ("adam", 1), ("wojtek", 2),
                   ("rysiek", 2), ("gerwazy", 1), key=lambda x: (-x[1], x[0]))


if __name__ == "__main__":
    main()
