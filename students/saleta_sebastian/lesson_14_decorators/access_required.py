from authorization import has_access
from functools import wraps


def access_required(func):
    @wraps(func)
    def wrap_func(name):
        if has_access(name):
            return func(name)
        else:
            return None
    return wrapp_func


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


def main():
    restricted_print('1 - visible')
    restricted_print('2 - invisible')
    restricted_print('3 - invisible')
    restricted_print('4 - visible')


if __name__ == '__main__':
    main()
