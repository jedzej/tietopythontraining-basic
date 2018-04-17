def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, val in kwargs.items():
        print("{}: {}".format(key, val))

