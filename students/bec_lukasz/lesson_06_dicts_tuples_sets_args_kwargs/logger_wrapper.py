def logger_wrapper(foo, *args, **kwargs):
    print('Passed args: ', end=' ')
    for arg in args:
        print(arg, end=', ')

    print()
    print('Passed kwargs: ', end=' ')
    for kwarg in kwargs:
        print(kwarg, ': ', kwargs[kwarg], end=', ')
    print()
    foo(*args, **kwargs)


def sth(*args, **kwargs):
    print('Method: ' + str(args) + str(kwargs))


logger_wrapper(sth, 1, 2, 3, cztery=4, piec=5)
