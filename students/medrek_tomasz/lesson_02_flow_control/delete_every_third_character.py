#!/usr/bin/env python3

s = input('Please enter a string:\n')
if not s:
    print('Empty string, try again')
    exit()

m = ""
for i in range(len(s)):
    if i % 3:
        m += s[i]

print(m)
