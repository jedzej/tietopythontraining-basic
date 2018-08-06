#!/usr/bin/env python3
"""Helper authorization script"""


from lesson_14_decorators.authorization import Access


def access_required(original_function):
    """Access decorator"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        if Access.has_access():
            original_function(*args, **kwargs)
    return wrapper


@access_required
def restricted_print(*args, **kwargs):
    """Restricted print function"""
    print(*args, **kwargs)


def main():
    """Main function"""
    restricted_print('1 - visible')
    restricted_print('2 - invisible')
    restricted_print('3 - invisible')
    restricted_print('4 - visible')


if __name__ == '__main__':
    main()
