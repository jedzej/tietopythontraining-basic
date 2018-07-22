import authorization


def access_required(some_function):
    def check_access(*args, **kwargs):
        if authorization.has_access():
            return some_function(*args, **kwargs)

    return check_access


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


restricted_print('1 - visible')
restricted_print('2 - invisible')
restricted_print('3 - invisible')
restricted_print('4 - visible')
