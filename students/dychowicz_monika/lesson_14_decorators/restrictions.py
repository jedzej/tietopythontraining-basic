import authorization


class AuthorizationError(Exception):
    pass


def access_required(func):
    def function_wrapper(*args, **kwargs):
        if not authorization.has_access():
            raise AuthorizationError
        return func(*args, **kwargs)
    return function_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == '__main__':
    data = [
        '1 - visible',
        '2 - invisible',
        '3 - invisible',
        '4 - visible'
    ]

    for item in data:
        try:
            restricted_print(item)
        except AuthorizationError:
            pass