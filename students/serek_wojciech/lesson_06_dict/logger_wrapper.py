#!/usr/bin/env python3
"""Arg inspector exercise"""
from args_inspector import inspect_args


def test_function(*args, **kwargs):
    """Just simple test function"""
    print('test_function:')
    print('Args"')
    print(args)
    print('Kwargs:')
    print(kwargs)


def logger_wrapper(function, *args, **kwargs):
    """Logger wrapper function"""
    print('logger_wrapper:')
    inspect_args(*args, **kwargs)
    function(*args, **kwargs)


def main():
    """Main function"""
    logger_wrapper(test_function, 1, 2, 3, 4, **{'one': 1, 'two': 2,
                                                 'three': 3})


if __name__ == '__main__':
    main()
