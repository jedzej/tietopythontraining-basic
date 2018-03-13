import math
from decimal import Decimal


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1 - y2, 2))


def program():
    x1 = Decimal(input())
    y1 = Decimal(input())
    x2 = Decimal(input())
    y2 = Decimal(input())
    print(distance(x1, y1, x2, y2))


if __name__ == '__main__':
    program()
