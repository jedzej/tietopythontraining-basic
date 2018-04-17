from math import sqrt


def length_of_segment(x1, y1, x2, y2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    except ValueError:
        print("You have to input a real number not a string")
    return length

print(length_of_segment(input(), input(), input(), input())
