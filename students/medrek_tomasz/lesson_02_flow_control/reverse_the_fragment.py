#!/usr/bin/env python3

s = input('Please enter a string:\n')
if not s:
    print('Empty string, try again')
    exit()
if s.count('h') < 2:
    print('Not enough "h" in given string, try again')
    exit()

first_h = s.find('h')
last_h = s.rfind('h')

print(s[:first_h]+s[last_h:first_h:-1]+s[last_h:])
