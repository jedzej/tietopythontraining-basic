
def foo(*args):
    pass


def logger_wrapper(foo, *args, **kwargs):

    for i, arg in enumerate(args):
        print("Arg {}: {}".format(str(i + 1), str(arg)))
        foo(arg)

    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
        foo(key, value)


if __name__ == '__main__':
    logger_wrapper(foo)
