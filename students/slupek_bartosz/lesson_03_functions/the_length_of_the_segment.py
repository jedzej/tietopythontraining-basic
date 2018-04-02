from math import sqrt


def length_of_segment(x1, y1, x2, y2):
    try:
        length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    except ValueError:
        print("You have to input a real number")
    return length

print(length_of_segment(float(input()), float(input()),
                        float(input()), float(input())))
