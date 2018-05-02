import math


def print_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def main():
    point1x = float(input())
    point1y = float(input())
    point2x = float(input())
    point2y = float(input())
    print_distance(point1x, point1y, point2x, point2y)


if __name__ == '__main__':
    main()
