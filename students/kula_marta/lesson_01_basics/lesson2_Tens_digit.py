#!/usr/bin/env python

a = input("set number: ")
s = str(a)
s_dig_cnt = 0
array_dig = []

for digit in s:
    array_dig.append(digit)

s_dig_cnt = len(array_dig)
print(array_dig[s_dig_cnt-2])


