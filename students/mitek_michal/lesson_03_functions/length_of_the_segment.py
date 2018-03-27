import math


def calculate_length_of_the_segment(x1, y1, x2, y2):

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(distance)
    return distance


x1_input, x2_input, y1_input, y2_input = float(input("Provide x1 ")),\
                                            float(input("Provide x2 ")),\
                                            float(input("Provide y1 ")),\
                                            float(input("Provide y2 "))

if __name__ == '__main__':
    calculate_length_of_the_segment(x1_input, x2_input, y1_input, y2_input)
