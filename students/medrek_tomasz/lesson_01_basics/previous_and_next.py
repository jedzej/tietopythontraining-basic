#!/usr/bin/env python3

try:
    given_number = int(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

previous_number = given_number - 1
next_number = given_number + 1

print("The next number for the number {0} is {1}.".format(
    given_number, next_number))
print("The previous number for the number {0} is {1}.".format(
    given_number, previous_number))
