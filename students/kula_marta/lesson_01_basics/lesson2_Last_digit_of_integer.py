#!/usr/bin/env python

a = int(input("set number: "))
b = a
s = str(a)
s_dig_cnt = 0
array_dig = []

for digit in s:
    array_dig.append(digit)
    s_dig_cnt = s_dig_cnt + 1

aa = array_dig[s_dig_cnt-1]
print(aa)