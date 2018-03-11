# check if knight can move to target position

import math

knight_x = int(input())
knight_y = int(input())
dest_x = int(input())
dest_y = int(input())

delta_x = knight_x - dest_x
delta_y = knight_y - dest_y
# lose direction vector (sign)
delta_x = math.fabs(delta_x)
delta_y = math.fabs(delta_y)

if delta_x == 2 and delta_y == 1 or delta_x == 1 and delta_y == 2:
    print("YES")
else:
    print("NO")
