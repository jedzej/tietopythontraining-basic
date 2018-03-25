from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


while True:
    try:
        x1coordinate = float(input("Type x1 coordinate: "))
        y1coordinate = float(input("Type y1 coordinate: "))
        x2coordinate = float(input("Type x2 coordinate: "))
        y2coordinate = float(input("Type y2 coordinate: "))
        print("The distance is:", distance(x1coordinate, y1coordinate,
                                           x2coordinate, y2coordinate))
        break
    except ValueError:
        print("All numbers must be real.")
        continue
