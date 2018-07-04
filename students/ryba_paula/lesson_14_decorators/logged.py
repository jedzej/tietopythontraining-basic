def logger_wrapper(func, *args, **kwargs):
    print("Args:")
    for arg in args:
        print(str(arg))

    print("Kwargs:")
    for key, val in kwargs.items():
        print("{0} : {1}".format(key, val))
    func(*args, **kwargs)


def logged(func):
    def func_wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def foo(*args, **kwargs):
    print("Foo function ", args, kwargs)


@logged
def write_sth(sth):
    print("Argument: {}".format(sth))


@logged
def write_nothing():
    print("\nNothing")


def main():
    dictionary = {'five': 5, 'six': 6}
    foo(1, 2, 3, 4, **dictionary)
    foo()
    foo(1)
    foo(**dictionary)
    print("\n")
    write_sth(1)
    write_sth("")
    print("\n")
    write_nothing()


if __name__ == '__main__':
    main()
