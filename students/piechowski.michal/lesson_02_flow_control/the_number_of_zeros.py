#!/usr/bin/env python3

numbers_count = int(input())
zeros_counter = 0

for i in range(0, numbers_count):
    number = int(input())
    if number == 0:
        zeros_counter += 1

print(zeros_counter)
