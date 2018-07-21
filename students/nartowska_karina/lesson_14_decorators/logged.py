from args_inspector import args_inspector


def logged(func):
    def logger_wrapper(*args, **kwargs):
        args_inspector(*args, **kwargs)
        return func(*args, **kwargs)
    return logger_wrapper


@logged
def verify_1(*args):
    print(args)


@logged
def verify_2(*args, **kwargs):
    print(*args, **kwargs)


@logged
def verify_3(name, surname):
    print('My name: ' + name)
    print('My surname: ' + surname)


verify_1('x', [0, 1])
verify_2("xyz", [0, 1, 2])
verify_3('Karina', 'Nartowska')
