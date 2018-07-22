def main():
    example_one('some', 'arguments', status='good')
    example_two('John')
    print(example_three(2, 5))


def logged(func):
    def wrap_func(*args, **kwargs):
        return wrap_logs(func, *args, **kwargs)
    return wrap_func


@logged
def example_one(*args, **kwargs):
    print(*args, **kwargs)


@logged
def example_two(name):
    print('Hello '.format(name))


@logged
def example_three(a, b):
    c = a + b
    print(c)
    return c


# from lesson 6
def wrap_logs(foo, *args, **kwargs):
    args_inspector(*args, **kwargs)
    return foo(*args, *kwargs)


def args_inspector(*args, **kwargs):
    print("Arguments:", end=" ")
    for value in args:
        print(value, end=" ")
    print("\n\nKey : Value pairs:")
    for key, value in kwargs.items():
        print("{0} : {1}".format(key, value))


if __name__ == '__main__':
    main()
