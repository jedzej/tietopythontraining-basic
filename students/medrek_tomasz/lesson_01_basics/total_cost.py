#!/usr/bin/env python3

given_numbers = []

for i in range(3):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

dollars = given_numbers[0]
cents = given_numbers[1]
cupcakes = given_numbers[2]

cost_in_cents = cupcakes * cents % 100
cost_in_dollars = cupcakes * cents // 100 + cupcakes * dollars

print(str(cost_in_dollars) + " " + str(cost_in_cents))
