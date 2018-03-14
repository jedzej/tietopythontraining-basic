"""
title: factorial
author: akasp@interia.pl, arkadiusz.kasprzyk@tieto.com
date: 2018-03-13
description: n!
"""

n = int(input("n = "))
factorial = 1

if n > 1:
    for k in range(1, n+1):
        factorial *= k

print(factorial)

print("")