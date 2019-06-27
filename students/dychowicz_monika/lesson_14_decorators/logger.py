import logger_wrapper


def logged(func):
    def function_wrapper(*args, **kwargs):
        return logger_wrapper.logger_wrapper(func, *args, **kwargs)
    return function_wrapper


@logged
def test_method_1():
    pass


@logged
def test_method_2():
    return 'foo'


@logged
def test_method_3(arg1, arg2):
    return arg1 + arg2


@logged
def test_method_4(*args):
    return [x for x in args]


@logged
def test_method_5(*args, **kwargs):
    return None


if __name__ == '__main__':
    test_method_1()
    test_method_2()
    test_method_3(1, 2)
    test_method_4(1, 4, 5, -3, 'aa')
    test_method_5(1, 4, 5, -3, 'aa', a=1, b=45, c='buz')