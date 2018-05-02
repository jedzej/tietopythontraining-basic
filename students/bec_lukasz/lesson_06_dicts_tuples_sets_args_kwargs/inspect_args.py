def inspect_args(*args, **kwargs):
    print('Passed args: ', end=' ')
    for arg in args:
        print(arg, end=', ')

    print()
    print('Passed kwargs: ', end=' ')
    for kwarg in kwargs:
        print(kwarg, ': ', kwargs[kwarg], end=', ')


inspect_args(1, 2, 3, 4, kwarg1='1', kwarg2='2')
