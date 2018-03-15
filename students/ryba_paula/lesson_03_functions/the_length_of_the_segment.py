from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def input_cooridnates():
    x1 = float(input("Type the row from the first coordinate: "))
    y1 = float(input("Type the column from the first coordinate: "))
    x2 = float(input("Type the row from the second coordinate: "))
    y2 = float(input("Type the column from the second coordinate: "))
    print("The distance is:", distance(x1, y1, x2, y2))


while True:
    try:
        input_cooridnates()
        break
    except ValueError:
        print("All numbers must be real")
        continue
