#!/usr/bin/env python3


from math import sqrt


def distance(x1, y1, x2, y2):
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return (distance)


def main():
    seq = ['x1', 'y1', 'x2', 'y2']
    coords = dict.fromkeys(seq)
    for key in seq:
        try:
            coords[key] = float(input(
                'Please enter value of {0} coordinate:\n'.format(key)))
        except ValueError:
            print('Not a valid number, try again')
            exit()

    print(distance(coords['x1'], coords['y1'], coords['x2'], coords['y2']))


if __name__ == "__main__":
    main()
