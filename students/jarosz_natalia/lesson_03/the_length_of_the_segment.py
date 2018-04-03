import math


def distance(a1, b1, a2, b2):
    dist = math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)
    return dist


def main():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    print(distance(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
