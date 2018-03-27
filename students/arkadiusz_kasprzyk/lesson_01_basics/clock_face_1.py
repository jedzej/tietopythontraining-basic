'''
title: clock_face_1
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
degs = H * deg_per_hour + (60 * M + S)/120

print("Angle (in deg) of the hour hand is {}".format(degs))

input("Press Enter to quit the program.")