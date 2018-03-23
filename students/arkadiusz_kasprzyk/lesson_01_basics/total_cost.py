'''
title: total_cost
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    A cupcake costs A dollars and B cents.
    Determine, how many dollars and cents should one pay for N cupcakes.
    A program gets three numbers: A, B, N.
    It should print two numbers: total cost in dollars and cents.
'''

import math as m
tol = 1e9  ## tolerance

print('''
    A cupcake costs A dollars and B cents. 
    Determine, how many dollars and cents should one pay for N cupcakes. 
    '''
)

A = int(input("dollars: "))
B = int(input("cents: "))
N = int(input("number of cupcakes: "))

dd = N*A
cc = N*B
dd_sum = dd + cc//100
cc_sum = cc % 100

print("{} cupcakes will cost {} dollars and {} cents".format(N, dd_sum, cc_sum))

input("Press Enter to quit the program.")