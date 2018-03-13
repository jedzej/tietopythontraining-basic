#!/usr/bin/env python3
minutes = int(input())
minutes = minutes % (24*60)
hours = minutes // 60
minutes = minutes % 60
print('{0:2d} {1:02d}'.format(hours, minutes))


  
