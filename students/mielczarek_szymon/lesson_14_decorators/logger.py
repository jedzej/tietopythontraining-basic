#! python3


def logger_wrapper(func, *args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(str(arg))

    print()
    print("Keyword arguments:")
    for key, val in kwargs.items():
        print("{}: {}".format(key, val))

    func(*args, **kwargs)


def logged(func):
    def func_wrapper(*args, **kwargs):
        logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def foo(*args, **kwargs):
    print("Foo function", args, kwargs)


@logged
def void():
    print("Void function without args")


def main():
    print("Test foo with some positional and keyword arguments")
    foo(1, "two", three="3")
    print("Test foo without arguments")
    foo()
    print("Test void without arguments")
    void()


if __name__ == '__main__':
    main()
