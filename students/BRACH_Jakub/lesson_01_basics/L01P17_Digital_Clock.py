#!/usr/bin/env python3
import math

print('Enter minutes')
minutes = int(input())

#remove full days
minutes = minutes % (24*60)

hours = minutes / 60
minutes = minutes % 60

print('The time is {0:d}:{1:02d}'.format(hours, minutes))


  
