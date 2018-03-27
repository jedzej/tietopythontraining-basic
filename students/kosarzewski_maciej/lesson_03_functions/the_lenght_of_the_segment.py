import math


def distance(x_value1, y_value1, x_value2, y_value2):
    dist = math.sqrt((x_value2 - x_value1) ** 2 + (y_value2 - y_value1) ** 2)
    return dist


x1 = float(input("Enter X1 position: "))
y1 = float(input("Enter Y1 position: "))
x2 = float(input("Enter X2 position: "))
y2 = float(input("Enter Y2 position: "))
print(distance(x1, y1, x2, y2))
