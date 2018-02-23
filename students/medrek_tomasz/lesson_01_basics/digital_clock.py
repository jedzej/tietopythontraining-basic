#!/usr/bin/env python3

try:
    given_number = int(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

hours = given_number // 60 % 24
minutes = given_number % 60

print(str(hours) + " " + str(minutes))
