def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg + ' - ' + kwargs[kwarg])


logger_wrapper(inspect_args, 1.0, 2, 4, 5, trzy=' 3', cztery='4')
