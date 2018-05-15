#!/usr/bin/env python

n = int(input("set minutes: "))
h = int(n / 60)
m = n - h * 60
print("how much hours and minutes show a digital clock %d : %d" % (h, m))
