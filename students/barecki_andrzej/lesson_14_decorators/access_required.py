from authorization import has_access


def access_required(func):
    def access_required_wrapper(*args, **kwargs):
        if has_access(*args):
            return func(*args, **kwargs)
        else:
            return func("No access. Data is not visible!!!")
    return access_required_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


def main():
    restricted_print('1 - visible')
    restricted_print('2 - invisible')
    restricted_print('3 - invisible')
    restricted_print('4 - visible')

    """"additional tests"""
    restricted_print('5 - visible', 6, 7)
    restricted_print('6 - invisible', 8, 9)


if __name__ == '__main__':
    main()
