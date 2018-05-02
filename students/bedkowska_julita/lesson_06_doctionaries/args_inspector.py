def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg + ' - ' + kwargs[kwarg])


inspect_args(1, 2.0, 3, jeden='1', dwa='2', trzy='3')
