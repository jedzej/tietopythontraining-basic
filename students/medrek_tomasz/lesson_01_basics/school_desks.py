#!/usr/bin/env python3

given_numbers = []
number_of_desks = 0

for i in range(3):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

    number_of_desks += given_numbers[i] // 2
    if (given_numbers[i] % 2):
        number_of_desks += 1

print(number_of_desks)
