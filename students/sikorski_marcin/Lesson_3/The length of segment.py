import math

def distance(x1,y1,x2,y2):
    distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return distance

first_x = float(input("Type first X: "))
first_y = float(input("Type first Y: "))
second_x = float(input("Type second X: "))
second_y = float(input("Type second Y: "))

print(distance(first_x,first_y,second_x,second_y))