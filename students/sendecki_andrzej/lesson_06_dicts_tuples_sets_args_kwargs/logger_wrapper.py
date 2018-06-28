# Logger wrapper - write a function called logger_wrapper
# that wraps call to any function in order to log passed args.
# The function must take foo, *args and **kwargs, prints *args
# and **kwargs in human readable format and finally call foo
# with args and kwargs


def myfunction(a, k):
    print(a, k)


def logger_wrapper(foo, *args, **kwargs):
    for a in args:
        print(a)

    for k, v in kwargs.items():
        print (k + ": " + str(v))

    foo(args, kwargs)


logger_wrapper(myfunction, 1, 2, city="Wroclaw", number=42)
