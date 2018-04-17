#!/usr/bin/env python

a = int(input("enter three-digit number: "))
s = str(a)
array_dig = []

for digit in s:
    array_dig.append(digit)

w = int(array_dig[0]) + int(array_dig[1]) + int(array_dig[2])
print("sum of this three digits are w = %d" % w)
