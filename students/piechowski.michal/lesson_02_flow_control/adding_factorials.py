#!/usr/bin/env python3

number = int(input())
factorial = 1
factorial_sum = 1

for i in range(2, number + 1):
    factorial *= i
    factorial_sum += factorial

print(factorial_sum)
