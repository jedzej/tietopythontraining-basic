#!/usr/bin/env python3

given_numbers = []

for i in range(3):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

hours = given_numbers[0]
minutes = given_numbers[1]
seconds = given_numbers[2]

seconds_passed = seconds + minutes * 60 + hours * 3600
full_circle_in_seconds = 12 * 3600
angle = float(360 * seconds_passed / full_circle_in_seconds)

print(angle)
