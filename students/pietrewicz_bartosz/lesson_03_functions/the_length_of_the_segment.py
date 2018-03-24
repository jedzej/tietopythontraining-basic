from math import sqrt


def distance(x1, y1, x2, y2):
    """Calculates distance between points.

    Arguments:
    x1 -- horizontal coordinate of first point
    y1 -- vertical coordinate of first point
    x2 -- horizontal coordinate of second point
    y2 -- vertical coordinate of second point
    """
    horiz_len = abs(x2 - x1)
    vert_len = abs(y2 - y1)
    return sqrt(horiz_len**2 + vert_len**2)


def main():
    # Read first point (x1, y1)
    x1 = float(input())
    y1 = float(input())
    # Read second point (x2, y2)
    x2 = float(input())
    y2 = float(input())
    # Calculate distance between points
    print(distance(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
