from students.jemielity_kamil.lesson_14_advanced_oop_and_decorators.authorization import has_access


def access_required(func):
    def function_wrapper(*args, **kwargs):
        if has_access() is True:
            func(*args, **kwargs)
    return function_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


restricted_print('1 - visible')
restricted_print('2 - invisible')
restricted_print('3 - invisible')
restricted_print('4 - visible')
