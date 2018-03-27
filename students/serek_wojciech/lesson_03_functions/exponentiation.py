#!/usr/bin/env python3
"""Exponentiation"""


def exponentiation(a_value, n_value):
    """Count recursively exponentiation a_value ^ n_value"""
    if n_value == 0:
        return 1

    return a_value * exponentiation(a_value, n_value - 1)


def main():
    """Main function"""
    a_value = float(input())
    n_value = int(input())

    print(exponentiation(a_value, n_value))


if __name__ == '__main__':
    main()
