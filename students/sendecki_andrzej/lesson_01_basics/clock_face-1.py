# lesson_01_basics
# Clock face - 1
# 
# Statement
# H hours, M minutes and S seconds are passed since the midnight
# (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# Determine the angle (in degrees) of the hour hand on the clock face right now.

print("Enter the number of hours")
h = int(input())
# it's a 12th part of 360 degree
angle_h = (h/12)*360

print("Enter the number of minutes")
m = int(input())
# it's a 12*60th (720) part of 360 degree
angle_m = (m/720)*360

print("Enter the number of seconds")
s = int(input())
# it's a 12*60*60th (43200) part of 360 degree
angle_s = (s/43200)*360

angle = angle_h + angle_m + angle_s

print("The angle of the hour hand is: " + str(angle))
