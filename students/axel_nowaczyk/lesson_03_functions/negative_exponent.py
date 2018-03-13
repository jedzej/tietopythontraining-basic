from decimal import Decimal


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


def program():
    a = Decimal(input())
    n = int(input())
    base_power = power(a, abs(n))
    if n < 0:
        print(1/base_power)
    else:
        print(base_power)


if __name__ == '__main__':
    program()

