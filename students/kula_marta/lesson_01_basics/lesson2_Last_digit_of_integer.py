#!/usr/bin/env python

a = input("set number: ")
b = a
s = str(a)
s_dig_cnt = 0
array_dig = []

for digit in s:
    array_dig.append(digit)
    s_dig_cnt = s_dig_cnt + 1

if (s_dig_cnt > 2):
    for x in range(s_dig_cnt - 2):
        b = b - int(array_dig[x]) * 10**(s_dig_cnt - x -1)
        if ((b >= 10) & (b < 99)):
            break

aa = b / 10
print(aa)