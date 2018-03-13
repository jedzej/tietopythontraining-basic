#!/usr/bin/env python3

number_of_pins, number_of_balls = [int(x) for x in input().split()]

pins = ['I'] * number_of_pins

for role in range(0, number_of_balls):
    knocked_down_start, knocked_down_end = [int(x) for x in input().split()]
    for i in range(knocked_down_start - 1, knocked_down_end):
        pins[i] = '.'

for i in range(0, number_of_pins):
    print(pins[i], end = '')

