#!/usr/bin/env python

a = int(input("enter the number of students in A class: "))
b = int(input("enter the number of students in B class: "))
c = int(input("enter the number of students in C class: "))

if (a % 2) == 0:
    x_a = a / 2
else:
    x_a = (a / 2) + 1

if (b % 2) == 0:
    x_b = b / 2
else:
    x_b = (b / 2) + 1

if (c % 2) == 0:
    x_c = c / 2
else:
    x_c = (c / 2) + 1

print("number of desks that can be purchased = %d" % (x_a + x_b + x_c))
