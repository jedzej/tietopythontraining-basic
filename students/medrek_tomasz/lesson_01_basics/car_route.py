#!/usr/bin/env python3

given_numbers = []

for i in range(2):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

kilometers_per_day = given_numbers[0]
whole_route = given_numbers[1]

if (whole_route % kilometers_per_day):
    minimum_days_to_travel = whole_route // kilometers_per_day + 1
else:
    minimum_days_to_travel = whole_route / kilometers_per_day

print(minimum_days_to_travel)
