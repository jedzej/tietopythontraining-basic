
def foo(*args):
    pass


def logger_wrapper(foo, *args, **kwargs):

    for arg in args:
        print(arg)
        foo(arg)

    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
        foo(key, value)


if __name__ == '__main__':
    logger_wrapper()
