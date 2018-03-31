import math


def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def main():
    x1 = float(input())
    x2 = float(input())
    y1 = float(input())
    y2 = float(input())

    print(distance(x1, x2, y1, y2))


if __name__ == '__main__':
    # `python hello_world.py` will run main(), `import hello_world` will not
    main()
