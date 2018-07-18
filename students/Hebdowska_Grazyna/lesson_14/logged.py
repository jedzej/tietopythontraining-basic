def logged(fun):
    def logger_wrapper(*args, **kwargs):
        print(args, kwargs)
        return fun(*args, *kwargs)
    return logger_wrapper


@logged
def inspect_args(*args):
    print (args)


@logged
def one(*args, **kwargs):
    print(*args, **kwargs)


@logged
def two(a, b, c):
    d = a + b - c
    print(d)
    return d


@logged
def three(name, age):
    print('This is ' + name)
    print(str(age) + ' - years old')


inspect_args('a', [1, 2])
one("ala", [1, 2, 3])
two(1, 2, 3)
three('Ala', 23)
