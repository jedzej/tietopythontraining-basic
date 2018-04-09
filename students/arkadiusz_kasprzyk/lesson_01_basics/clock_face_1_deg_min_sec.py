'''
title: clock_face_1_deg_min_sec
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
    Determine the angle (in degrees) of the hour hand on the clock face right now.
'''

import math as m
print('''
    H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). 
    Determines the angle (in degrees) of the hour hand on the clock face right now.
''')

H = int(input("hours: "))
M = int(input("minutes: "))
S = int(input("seconds: "))

deg_per_hour = 30  ## = 360/12
min_per_minute = 30 ## 1/2  deg_per_minute = 30/60
sec_per_second = 30 ## 1/2  min per second = 30/60

degs = H * deg_per_hour
mins = M * min_per_minute
secs = S * sec_per_second


mins = mins + secs // 60
secs = secs % 60

degs = degs + mins // 60
mins = mins % 60


print("Angle (in deg.min.sec) of the hour hand is {}° {}' {}''".format(degs, mins, secs))

input("Press Enter to quit the program.")