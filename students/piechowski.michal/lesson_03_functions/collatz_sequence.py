#!/usr/bin/env python3


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print("Give number for collatz function:")
try:
    number = int(input())
except ValueError:
    print("You must input an integer!")
    quit()

if number < 1:
    print("Wrong number, it needs to be >= 1")
    quit()

while True:
    number = collatz(number)
    if number == 1:
        break
