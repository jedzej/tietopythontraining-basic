def inspect_args(*args, **kwargs):
    for i in args:
        print(i)
    for j in kwargs:
        print("{} : {}".format(j, kwargs[j]))


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    return foo(*args, **kwargs)


def logged(func):
    def func_wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def foo_1(*args, **kwargs):
    return sum(args)


@logged
def foo_2(*args, **kwargs):
    return '-'.join(i for i in kwargs.values())


@logged
def foo_3(*args, **kwargs):
    separator = '-(^o^)-'
    args_str = separator.join(str(i) for i in args)
    kwargs_str = separator.join(i for i in kwargs.values())
    return args_str + separator + kwargs_str


for foo in [foo_1, foo_2, foo_3]:
    print(foo(1, 2, 3, 4, 5, 6, first="1", second="2"))
