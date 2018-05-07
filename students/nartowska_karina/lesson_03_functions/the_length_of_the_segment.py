from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def main():
    print("Enter four real numbers representing cartesian coordinates")
    print("x1 is: ")
    x1 = float(input())
    print("y1 is: ")
    y1 = float(input())
    print("x2 is: ")
    x2 = float(input())
    print("y2 is: ")
    y2 = float(input())
    print("The distance is:")
    print(distance(x1, y1, x2, y2))


if __name__ == "__main__":
    main()
