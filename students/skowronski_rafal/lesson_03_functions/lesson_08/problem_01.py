# Solves 'The length of the segment' problem


def _distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def _main():
    x1 = float(input('Enter x\u2081 coordinate: '))
    y1 = float(input('Enter y\u2081 coordinate: '))

    x2 = float(input('Enter x\u2082 coordinate: '))
    y2 = float(input('Enter y\u2082 coordinate: '))

    distance = _distance(x1, y1, x2, y2)

    print('Distance between points is: {0}'.format(distance))


if __name__ == '__main__':
    _main()
