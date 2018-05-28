from args_inspector import inspect_args


def sum_all(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def foo(*args, **kwargs):
    print("Foo:\n args:", args, "\n kwargs: ", kwargs)


print(sum_all(2, 8, 5.7))
logger_wrapper(foo, 11, second=2, third='a')
