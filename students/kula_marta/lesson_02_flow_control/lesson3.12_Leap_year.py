#!/usr/bin/env python

a = int(input("set year: "))

if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print('LEAP')
else:
    print('COMMON')
