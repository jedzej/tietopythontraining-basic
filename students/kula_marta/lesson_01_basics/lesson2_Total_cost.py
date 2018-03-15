#!/usr/bin/env python

A = input("enter dollar: ")
B = input("enter cent: ")
c = input("the number of cupcakes: ")
x = A * c
y = B * c

if (y > 100):
    y_cnt = y / 100
    y = y - 100 * y_cnt
    x = x + y_cnt

print("%d.%d" % (x, y))