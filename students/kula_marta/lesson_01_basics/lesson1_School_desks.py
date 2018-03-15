#!/usr/bin/env python

a = input("enter the number of students in A class: ")
b = input("enter the number of students in B class: ")
c = input("enter the number of students in C class: ")

if      ((a % 2) == 0):
        w_a = a / 2
else:
        w_a = (a / 2) + 1

if      ((b % 2) == 0):
        w_b = b / 2
else:
        w_b = (b / 2) + 1

if      ((c % 2) == 0):
        w_c = c / 2
else:
        w_c = (c / 2) + 1

print(w_a + w_b + w_c)