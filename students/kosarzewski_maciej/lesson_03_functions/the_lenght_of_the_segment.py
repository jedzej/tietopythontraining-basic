import math


def distance(x_value1, y_value1, x_value2, y_value2):
    dist = math.sqrt((x_value2 - x_value1) ** 2 + (y_value2 - y_value1) ** 2)
    return dist


print ("Enter X1 position: ")
x1 = float(input())
print ("Enter Y1 position: ")
y1 = float(input())
print ("Enter X2 position: ")
x2 = float(input())
print ("Enter Y2 position: ")
y2 = float(input())
print(distance(x1, y1, x2, y2))
