import math


def distance(_ax, _ay, _bx, _by):
    ax = float(_ax)
    ay = float(_ay)
    bx = float(_bx)
    by = float(_by)
    result = math.sqrt(((bx - ax) ** 2) + ((by - ay) ** 2))
    return result


def main():

    x1 = input()
    y1 = input()
    x2 = input()
    y2 = input()

    dist = distance(x1, y1, x2, y2)
    print(dist)


if __name__ == '__main__':
    main()
