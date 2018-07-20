def main():
    example_one('bim', 'bam', status='bom')
    example_two('Bob')


def logged(func):
    def wrap_func(*args, **kwargs):
        return wrap_logs(func, *args, **kwargs)
    return wrap_func


@logged
def example_one(*args, **kwargs):
    print(*args, **kwargs)


@logged
def example_two(name):
    print('Hello ' + name)


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
