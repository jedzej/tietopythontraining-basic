#!/usr/bin/env python3
"""Logged decorator exercise"""
from lesson_06_dict.args_inspector import inspect_args


def logged(original_function):
    """Logged decorator"""
    def wrapper(*args, **kwargs):
        """Wrapper"""
        inspect_args(*args, **kwargs)
        return original_function(*args, **kwargs)
    return wrapper


@logged
def test_function(*args, **kwargs):
    """Just simple test function"""
    print('test_function:')
    print('Args"')
    print(args)
    print('Kwargs:')
    print(kwargs)


@logged
def is_equal(a, b):
    """Test function"""
    return a == b


def main():
    """Main function"""
    test_function(1, 2, 3, 4, **{'one': 1, 'two': 2, 'three': 3})
    print(is_equal(2, 5))
    print(is_equal(1, 1))

if __name__ == '__main__':
    main()
