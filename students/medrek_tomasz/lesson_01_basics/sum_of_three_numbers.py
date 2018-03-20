#!/usr/bin/env python3

given_numbers = []

for i in range(3):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

sum_of_three_numbers = sum(given_numbers)
print(sum_of_three_numbers)
