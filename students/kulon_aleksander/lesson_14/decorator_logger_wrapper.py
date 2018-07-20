from lesson_06.args_inspector import args_inspect


def wrap_logs(foo, *args, **kwargs):
    args_inspect(*args, **kwargs)
    return foo(*args, *kwargs)


def logged(func):
    def wrap_func(*args, **kwargs):
        return wrap_logs(func, *args, **kwargs)
    return wrap_func


@logged
def function_1(*args, **kwargs):
    print(*args, **kwargs)


@logged
def function_add(a, b):
    result = a + b
    print(result)
    return result


@logged
def function_subtract(a, b):
    result = a - b
    print(result)
    return result


def main():
    function_1('Example', 'strings', 'for', 'test', 'purposes')
    function_add(2, 2)
    function_subtract(5, 3)


if __name__ == '__main__':
    main()
