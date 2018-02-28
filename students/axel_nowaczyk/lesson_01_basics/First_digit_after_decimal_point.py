from decimal import Decimal


def first_digit():
    a = Decimal(input())
    frac = str(a-int(a))
    if len(frac) < 2:
        print(0)
    else:
        print(frac[2])


if __name__ == '__main__':
    first_digit()