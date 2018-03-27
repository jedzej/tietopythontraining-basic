#!/usr/bin/env python3
"""Negative exponent"""


def power(a_value, n_value):
    """Compute a^n"""
    result = 1

    for _ in range(abs(n_value)):
        result *= a_value

    if n_value > 0:
        return result
    return 1 / result


def main():
    """Main function"""
    print(power(float(input()), int(input())))


if __name__ == '__main__':
    main()
