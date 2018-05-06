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


if __name__ == "__main__":
    print("----------")
    args_inspector()
    print("----------")
    args_inspector(1)
    print("----------")
    args_inspector(1, 2)
    print("----------")
    args_inspector(a="A", b="B")
    print("----------")
    args_inspector(1, 2, a="A", b="B")
    print("----------")
    args_inspector(a="A", b="B")
    print("----------")
