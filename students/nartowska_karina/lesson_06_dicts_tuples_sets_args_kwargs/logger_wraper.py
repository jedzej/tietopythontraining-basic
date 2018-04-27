from args_inspector import args_inspector


def logger_wrapper(foo, *args, **kwargs):
    args_inspector(*args, **kwargs)
    foo(args, kwargs)


def foo(*args, **kwargs):
    print("Test ended")


def main():
    print("Result:")
    logger_wrapper(foo, 1, name="Karina", surname="Nartowska")


if __name__ == '__main__':
    main()
