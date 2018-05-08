from args_inspector import inspect_args


def foo(*args, **kwargs):
    print("This is a foo function")
    print(args)
    print(kwargs)


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def main():
    logger_wrapper(foo, 1, 2, 3, **{'four' : 4, 'five' : 5})


if __name__ == '__main__':
    main()
