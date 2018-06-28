from args_inspector import inspect_args


def sum_all(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def together(*args, **kwargs):
    print("Foo:\n args:", args, "\n kwargs: ", kwargs)


logger_wrapper(together, 11, second=2, third='a')
