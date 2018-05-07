#!/usr/bin/env python3

number = int(input())
factorial = 1

for i in range(2, number + 1):
    factorial *= i

print(factorial)
