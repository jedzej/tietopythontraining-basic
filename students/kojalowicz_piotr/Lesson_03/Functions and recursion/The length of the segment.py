import math


def input_number():
    no = None
    while no is None:
        try:
            no = float(input())
        except ValueError:
            print('must enter an float')
    return no


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = input_number()
y1 = input_number()
x2 = input_number()
y2 = input_number()
print(distance(x1, y1, x2, y2))
