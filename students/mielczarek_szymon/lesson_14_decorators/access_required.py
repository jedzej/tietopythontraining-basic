#! python3
from functools import wraps
from students.mielczarek_szymon.lesson_14_decorators.authorization import has_access


def access_required(func):
    @wraps(func)
    def func_wrapper(name):
        if has_access(name):
            return func(name)
        else:
            return None
    return func_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


restricted_print('1 - visible')
restricted_print('2 - invisible')
restricted_print('3 - invisible')
restricted_print('4 - visible')
