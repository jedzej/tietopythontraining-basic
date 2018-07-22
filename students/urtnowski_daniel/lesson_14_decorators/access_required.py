#!/usr/bin/env python3

"""
access_required.py: a practice project number 2 from:
Lesson 14 - Decorators

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import authorization


def access_required(fun):
    """
    This function is a decorator that when applied to a function executes
    subjected function only if has_access function from authorization module
     returns True
    :param fun: reference to a function object
    """
    def wrapper(*args, **kwargs):
        if authorization.has_access():
            return fun(*args, **kwargs)
    return wrapper


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
