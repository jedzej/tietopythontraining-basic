#!/usr/bin/env python3

try:
    given_number = int(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

tens_digit = given_number % 100 // 10
print(tens_digit)
