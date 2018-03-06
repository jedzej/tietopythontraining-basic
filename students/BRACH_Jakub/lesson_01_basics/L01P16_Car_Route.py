#!/usr/bin/env python3
import math

print('Enter km per day')
daily = float(input())

print('Enter whole distance')
distance = float(input())

days_i = int (math.ceil(distance / daily))

print('It will take  {0:d} days'.format(days_i))


  
