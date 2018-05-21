def sum_all(*args):
    return sum(args)


def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)
    print("format - key : value")
    for k, v in kwargs.items():
        print("{}: {}".format(k, v))


# I ain't sure if I can use inspect_args, so I copied it below too. :)

def logger_wrapper(foo, *args, **kwargs):
    for arg in args:
        print(arg)
    print("format - key : value")
    for k, v in kwargs.items():
        print("{}: {}".format(k, v))

    foo(*args, **kwargs)


def foo(*args, **kwargs):
    pass
