'''
title: fractional_part
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Given a positive real number, print its fractional part.
'''

import math as m
print("Given a positive real number, prints its fractional part.")

x = float(input("Give a number: "))

f =  m.floor(x)
r = x - f


print("The fractional part is {}".format(r))

input("Press Enter to quit the program.")