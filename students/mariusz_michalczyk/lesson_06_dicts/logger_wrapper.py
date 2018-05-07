def foo(*args, **kwargs):
    print("Foo funtcion result: ")
    print(args[0] + args[1])


def logger_wrapper(foo, *args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)
    foo(*args, **kwargs)

print(logger_wrapper(foo, "<", "log1"))
