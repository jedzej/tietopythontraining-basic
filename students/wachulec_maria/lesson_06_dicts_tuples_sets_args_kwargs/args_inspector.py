def inspect_args(*args, **kwargs):
    for i in args:
        print(i)
    for j in kwargs:
        print("{} : {}".format(j, kwargs[j]))


inspect_args(1, 2, 3, 4, 5, 6, first="1", second="2")
