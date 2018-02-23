#!/usr/bin/env python3

given_numbers = []

for i in range(2):
    try:
        given_numbers.append(float(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

area_of_right_angled_triangle = given_numbers[0] * given_numbers[1] / 2
print(area_of_right_angled_triangle)
