#!/usr/bin/env python

n = int(input("set max km/day: "))
m = int(input("treap distanse: "))
if (m % n) == 0:
    x = m / n
else:
    x = m / n + 1

print("number of days to cover the rout = %d" % x)
