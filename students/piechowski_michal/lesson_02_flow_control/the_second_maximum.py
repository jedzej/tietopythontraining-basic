#!/usr/bin/env python3

maximum = -1
second_maximum = -1

while True:
    number = int(input())

    if number > maximum:
        second_maximum = maximum
        maximum = number
    elif number > second_maximum:
        second_maximum = number

    if number == 0:
        break

print(second_maximum)
