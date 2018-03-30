from decimal import Decimal


def fractal_part():
    number = Decimal(input())
    print(number - int(number))


if __name__ == '__main__':
    fractal_part()