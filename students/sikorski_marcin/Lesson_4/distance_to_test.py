from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if __name__== '__main__':
    try:
        x1 = float(input("Type value X1: "))
        y1 = float(input("Type value Y1: "))
        x2 = float(input("Type value X2: "))
        y2 = float(input("Type value Y2: "))
        result = distance(x1, y1, x2, y2)
        print(result)
    except ValueError:
        print("This is not a number")
