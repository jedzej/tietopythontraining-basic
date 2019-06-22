from authorization import has_access


def access_required(fun):
    def access_wrapper(*args, **kwargs):
        if has_access() is True:
            return fun(*args, **kwargs)

    return access_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


restricted_print('1 - visible')
restricted_print('2 - invisible')
restricted_print('3 - invisible')
restricted_print('4 - visible')
