from decimal import Decimal


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


def program():
    a = Decimal(input())
    n = int(input())
    print(power(a, n))


if __name__ == '__main__':
    program()