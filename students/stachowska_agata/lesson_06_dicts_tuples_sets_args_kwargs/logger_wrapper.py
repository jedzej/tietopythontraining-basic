from args_inspector import inspect_args
from args_sum import sum_all


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def foo(*args, **kwargs):
    print("Foo function:\n args:", args, "\n kwargs: ", kwargs)


print(sum_all(2, 8, 5.7))
logger_wrapper(foo, 55, second=2, third='a')
