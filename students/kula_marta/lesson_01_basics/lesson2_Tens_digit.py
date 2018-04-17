#!/usr/bin/env python

a = int(input("enter number: "))
s = str(a)
s_dig_cnt = 0
array_dig = []

for digit in s:
    array_dig.append(digit)

s_dig_cnt = len(array_dig)
print("how many tens digit is in enter number s_dig_cnt = %s"
      % array_dig[s_dig_cnt - 2])
