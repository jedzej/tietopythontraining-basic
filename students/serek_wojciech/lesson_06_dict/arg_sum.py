#!/usr/bin/env python3
"""Arg sum exercise"""


def arg_sum(*args):
    """Sum all arguments"""
    return sum(args)


def main():
    """Main function"""
    print(arg_sum(1, 2, 3, 4))
    print(arg_sum(1, 1))
    print(arg_sum(10, 20, 30, 40, 50))


if __name__ == '__main__':
    main()
