from students.jemielity_kamil.lesson_06_dicts_tuples_sets_args_kwargs \
    .args_inspector import inspect_args


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def logged(func):
    def function_wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return function_wrapper


@logged
def function_1(*args):
    print(*args)


@logged
def function_2(*args, **kwargs):
    print(*args, **kwargs)


@logged
def function_3(a, b):
    return a % b


@logged
def function_4(a, b, c, d):
    return a + b + c + d


@logged
def function_5(a, b):
    return a - b


function_1("raz", "dwa", "trzy")
function_2("a", "b", "c", [1, 2, 3], {"name": "John", "age": 30})
function_3(2, 3)
function_4(1, 2, 3, 4)
function_5(10, 11)
