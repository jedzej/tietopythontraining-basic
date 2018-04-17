def function_foo(*args, **kwargs):
    print("args: {}\n kwargs: {}".format(args, kwargs))


def logger_wrapper(foo, *args, **kwargs):
    for arg in args:
        print(arg)
    for key, val in kwargs.items():
        print("{}: {}".format(key, val))
    foo(*args, **kwargs)