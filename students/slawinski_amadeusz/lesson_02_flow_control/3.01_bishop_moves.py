# check if bishop can move to target position

import math

bishop_x = int(input())
bishop_y = int(input())
dest_x = int(input())
dest_y = int(input())

delta_x = bishop_x - dest_x
delta_y = bishop_y - dest_y
# time to compare if we move the same amount in both directions
# to do this just lose direction vector (sign)
delta_x = math.fabs(delta_x)
delta_y = math.fabs(delta_y)

if delta_x == delta_y:
    print("YES")
else:
    print("NO")
