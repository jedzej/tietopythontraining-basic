"""
Write @logged decorator using logger_wrapper
from lesson 6. Apply it to several functions
to demonstrate that it works.
"""


def logger_wrapper(func, *args, **kwargs):
    print("*args:")
    for i in args:
        print(i)
    print("**kwargs:")
    for key, val in kwargs.items():
        print(str(key) + ": " + str(val))

    func(*args, **kwargs)


def logged(func):
    def wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return wrapper


@logged
def foo_1():
    print("foo_1")


@logged
def foo_2(arg1, arg2, arg3):
    print("foo_2")
    if arg1 + arg2 > 10:
        print(arg3)


@logged
def foo_3(arg1, arg2, arg3, arg4, **kwargs):
    print("foo_3")
    print(str(arg1 + arg2 + arg3) + " " + arg4)


def main():
    """ No arguments """
    foo_1()
    """ Three args """
    foo_2(6, 6, "It works!")
    """ Four args, two kwargs """
    foo_3(1, 1, 1, "This one too", end='', reverse=True)


if __name__ == '__main__':
    main()
