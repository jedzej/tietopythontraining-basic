import math
H = int(input())
M = int(input())
S = int(input())

total = 60 * 60 * 12
current = S + (M * 60) + (H * 60 * 60)
ang = (current * 360) / total
x = round(ang, 5) - ang
per = (x * 10000000) / ang
if per == 0:
    if int(ang) == ang:
        print(int(ang))
    else:
        print(ang)
elif math.fabs(per) < 1:
    print(round(ang, 3))
elif math.fabs(per) < 100:
    print(round(ang, 5))
else:
    print(round(ang, 8))
