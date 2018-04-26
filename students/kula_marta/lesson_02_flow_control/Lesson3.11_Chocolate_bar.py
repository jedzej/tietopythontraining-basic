#!/usr/bin/env python

n = int(input())
m = int(input())
k = int(input())

if k <= m * n and (k % m == 0 or k % n == 0):
    print('YES')
else:
    print('NO')
