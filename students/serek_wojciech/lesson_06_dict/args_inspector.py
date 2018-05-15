#!/usr/bin/env python3
"""Arg inspector exercise"""


def inspect_args(*args, **kwargs):
    """Sum all arguments"""
    print('Args:')
    for i in range(len(args)):
        print('Arg ' + str(i) + ": " + str(args[i]))

    print("Kwargs:")
    cnt = 0
    for key, val in kwargs.items():
        print("Kwarg " + str(cnt) + ": " + str(key) + " : " + str(val))
        cnt += 1


def main():
    """Main function"""
    inspect_args(1, 2, 3, 4, **{'one': 1, 'two': 2, 'three': 3})


if __name__ == '__main__':
    main()
