#!/usr/bin/env python3


def args_inspector(*args, **kwargs):
    if not args and not kwargs:
        print("No arguments passed")

    if args:
        print("Passed arguments are:")
        for arg in args:
            print(arg)

    if kwargs:
        print("Passed keyword arguments are:")
        for k, v in kwargs.items():
            print(k, "=", v)


def logger_wrapper(foo, *args, **kwargs):
    args_inspector(*args, **kwargs)
    foo(*args, **kwargs)


def some_function(*args, **kwargs):
    print("Called some function")
    print(args)
    print(kwargs)


if __name__ == "__main__":
    logger_wrapper(some_function, 1, 2, a="A", b="B")
