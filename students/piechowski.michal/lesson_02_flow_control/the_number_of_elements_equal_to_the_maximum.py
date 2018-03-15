#!/usr/bin/env python3

maximum = -1
maximums_counter = 1

while True:
    number = int(input())

    if number > maximum:
        maximum = number
        maximums_counter = 1
    elif number == maximum:
        maximums_counter += 1

    if number == 0:
        break

print(maximums_counter)
