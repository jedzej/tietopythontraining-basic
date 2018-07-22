from lesson_06.args_inspector import inspect_args


def logged(func):
    def wrap_func(*args, **kwargs):
        return wrap_logs(func, *args, **kwargs)
    return wrap_func


def wrap_logs(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    return foo(*args, **kwargs)


@logged
def function_empty(*args, **kwargs):
    print(*args, **kwargs)


@logged
def function_concatenate(str1, str2):
    result = str1 + str2
    print(result)
    return result


@logged
def function_multiply(a, b):
    result = a * b
    print(result)
    return result


def main():
    function_empty('Just', 'some', 'text', '.')
    function_concatenate('concatenate', 'strings')
    function_multiply(3, 7)


if __name__ == '__main__':
    main()
