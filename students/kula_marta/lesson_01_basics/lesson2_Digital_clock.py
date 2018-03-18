#!/usr/bin/env python

n = int(input("set minutes: "))
h = int(n/60)
m = n - h*60

print("%d : %d" % (h, m))