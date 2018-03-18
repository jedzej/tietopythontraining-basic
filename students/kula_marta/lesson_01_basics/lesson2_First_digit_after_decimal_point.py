#!/usr/bin/env python

a = float(input("set float number: "))
u = a - int(a)
c = int(a)

if (u == 0):
    w = 0
else:
    s = str(round(u,2))
    array_dig = []

    for digit in s:
        array_dig.append(digit)
    w = int(array_dig[2])

print(w)