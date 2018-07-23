from lesson_06.logger_wrapper import logger_wrapper


def logged(func):
    def func_wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def first_function(*args, **kwargs):
    return str(args), str(kwargs)


@logged
def second_function():
    return None


print(first_function(1, 2, osiem=8))
print(second_function())
