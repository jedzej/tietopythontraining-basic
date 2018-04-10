#!/usr/bin/env python3

numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

min_number = min(numbers)
max_number = max(numbers)
min_index = numbers.index(min_number)
max_index = numbers.index(max_number)

numbers[min_index] = max_number
numbers[max_index] = min_number

for number in numbers:
    print(number, end=' ')
