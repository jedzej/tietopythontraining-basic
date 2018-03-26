import math


def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))


def main():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    print(distance(x1, x2, y1, y2))


if __name__ == '__main__':
    main()
