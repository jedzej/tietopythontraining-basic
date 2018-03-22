# The length of the segment
def distance(x1, y1, x2, y2):
    distance_of_points = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)
    return distance_of_points

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(distance(x_1, y_1, x_2, y_2))
