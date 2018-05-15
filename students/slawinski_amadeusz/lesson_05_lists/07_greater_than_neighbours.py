#!/usr/bin/env python3

count = 0

numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(1, len(numbers) - 1):
    if numbers[i - 1] < numbers[i] and numbers[i] > numbers[i + 1]:
        count = count + 1

print(count)
