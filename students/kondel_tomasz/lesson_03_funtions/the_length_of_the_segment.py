import math


def distance(ax, ay, bx, by):
    result = math.sqrt(((bx - ax) ** 2) + ((by - ay) ** 2))
    return result


def main():

    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    dist = distance(x1, y1, x2, y2)
    print(dist)


if __name__ == '__main__':
    main()
