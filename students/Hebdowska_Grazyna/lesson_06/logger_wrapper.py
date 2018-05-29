def logger_wrapper(foo, *args, **kwargs):
    print(args, kwargs)
    foo(*args, *kwargs)


def inspect_args(*args):
    print(args)


logger_wrapper(inspect_args, 'a', 2, {"1": 2})
