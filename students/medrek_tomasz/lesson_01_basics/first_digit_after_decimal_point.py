#!/usr/bin/env python3

try:
    given_number = float(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

real_part, fractional_part = str(given_number).split(".")

if (fractional_part == "0"):
    print("0")
else:
    print(fractional_part[0])
