#!/usr/bin/env python3
import math

print('Enter the hour hand angle')
hour_angle = float(input())



minute_angle = (hour_angle * 12) % 360


print('minute angle will be {0:f} deg.'.format(minute_angle))


  
