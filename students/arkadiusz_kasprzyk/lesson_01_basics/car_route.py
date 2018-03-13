'''
title: car_route
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    A car can cover distance of N kilometers per day.
    How many days will it take to cover a route of length M kilometers?
    The program gets two numbers: N and M.
'''

import math as m
tol = 1e-9  ## tolerance

print('''
    A car can cover distance of N kilometers per day.
    How many days will it take to cover a route of length M kilometers?
    '''
)

N = float(input("Number of km per day: "))
M = float(input("Number of km to cover: "))

f = m.floor(M/N)
r = f + int(abs(M-f) > tol)

print("It will take {} days to cover this route.".format(r))

input("Press Enter to quit the program.")