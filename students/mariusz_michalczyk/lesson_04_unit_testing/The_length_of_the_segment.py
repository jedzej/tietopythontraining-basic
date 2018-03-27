from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    x1 = abs(float(input()))
    y1 = abs(float(input()))
    x2 = abs(float(input()))
    y2 = abs(float(input()))
    print(distance(x1, y1, x2, y2))
