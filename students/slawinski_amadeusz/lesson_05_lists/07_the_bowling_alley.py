#!/usr/bin/env python3

readline = input().split()

pins_no = int(readline[0])
rolls = int(readline[1])

pins = ['I'] * pins_no

for i in range(rolls):
    readline = input().split()
    start = int(readline[0])
    end = int(readline[1])
    for i in range(start - 1, end):
        pins[i] = '.'

print(''.join(pins))
