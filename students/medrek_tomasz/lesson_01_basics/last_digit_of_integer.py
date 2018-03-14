#!/usr/bin/env python3

try:
    given_number = int(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

last_digit_of_integer = given_number % 10
print(last_digit_of_integer)
