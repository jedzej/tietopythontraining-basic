#!/usr/bin/env python3

s = input('Please enter a string:\n')
if not s:
    print('Empty string, try again')
    exit()

print(s.replace('@', ''))
