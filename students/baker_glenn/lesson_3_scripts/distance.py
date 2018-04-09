from math import sqrt


def distance(x1, y1, x2, y2):
    print(sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))


while True:
    try:
        print("Please enter the x coordinate of point 1")
        point_1_x = float(input())
        print("Please enter the y coordinate of point 1")
        point_1_y = float(input())
        print("Please enter the x coordinate of point 2")
        point_2_x = float(input())
        print("Please enter the y coordinate of point 2")
        point_2_y = float(input())
        break
    except:
        print("Please enter a real number")

distance(point_1_x, point_1_y, point_2_x, point_2_y)
