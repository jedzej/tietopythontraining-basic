import pprint


def foo(*args, **kwargs):
    print("Foo funtcion result: ")
    print(args[0] + args[1])


def logger_wrapper(foo, *args, **kwargs):
    pprint.pprint(args)
    pprint.pprint(kwargs)
    foo(*args, **kwargs)


if __name__ == '__main__':
    print(logger_wrapper(foo, "<", "log1"))
