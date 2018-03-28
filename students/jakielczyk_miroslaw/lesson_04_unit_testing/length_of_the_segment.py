# The length of the segment
import math


def main():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    print(distance(x1, y1, x2, y2))


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


if __name__ == "__main__":
    main()

