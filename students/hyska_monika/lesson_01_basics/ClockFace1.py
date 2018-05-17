# The program print the angle (in degrees) of the hour hand on the clock

H = int(input("Put hours: "))
M = int(input("Put minutes: "))
S = int(input("Put seconds: "))

S_sum = S + M * 60 + H * 3600   # change to seconds

H_st = 30 / 3600 * S_sum    # 1h = 30 degree, 360/12

print("For putted hour, angle of the hour hand is:", H_st)
