from math import sqrt


def distance(a1, b1, a2, b2):
    return sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)


if __name__ == "__main__":
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    print(distance(x1, y1, x2, y2))

