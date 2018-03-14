# check if queen can move to target position

import math

queen_x = int(input())
queen_y = int(input())
dest_x = int(input())
dest_y = int(input())

delta_x = queen_x - dest_x
delta_y = queen_y - dest_y
# time to compare if we move the same amount in both directions
# to do this just lose direction vector (sign)
delta_x = math.fabs(delta_x)
delta_y = math.fabs(delta_y)

if delta_x == delta_y or delta_x == 0 or delta_y == 0:
    print("YES")
else:
    print("NO")
