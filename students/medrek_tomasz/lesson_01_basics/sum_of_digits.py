#!/usr/bin/env python3

try:
    given_number = int(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

if (given_number // 100) and not (given_number // 1000):
    sum_of_digits = given_number // 100
    sum_of_digits += given_number % 100 // 10
    sum_of_digits += given_number % 10
else:
    print('That was not a valid number, please try again with three digits')
    exit()

print(sum_of_digits)
