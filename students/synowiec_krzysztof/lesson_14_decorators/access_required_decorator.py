from authorization import has_access


def main():
    restricted_print('1 - visible')
    restricted_print('2 - invisible')
    restricted_print('3 - invisible')
    restricted_print('4 - visible')


def access_required(func):
    def func_wrapper(*args, **kwargs):
        if has_access():
            func(*args, **kwargs)
    return func_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == '__main__':
    main()
