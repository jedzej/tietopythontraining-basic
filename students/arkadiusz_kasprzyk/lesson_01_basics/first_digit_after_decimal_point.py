'''
title: first_digit_after_decimal_point
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Given a positive real number, print its first digit to the right of the decimal point.
'''

import math as m
print("Given a positive real number, prints its first digit to the right of the decimal point.")

x = float(input("Give a number: "))

f =  m.floor(x)
r = m.floor((x - f)*10)

print("The first digit after decimal point is {}".format(r))

input("Press Enter to quit the program.")