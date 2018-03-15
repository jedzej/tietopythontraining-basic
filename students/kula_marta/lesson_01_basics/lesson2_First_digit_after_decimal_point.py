#!/usr/bin/env python

a = float(raw_input("set float number: "))
u = a - int(a)

if (u == 0):
    w = 0
else:
    s = str(u)
    array_dig = []

    for digit in s:
        array_dig.append(digit)
    w = int(array_dig[2])

print(w)