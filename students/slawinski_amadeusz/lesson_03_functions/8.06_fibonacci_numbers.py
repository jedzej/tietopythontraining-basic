#!/usr/bin/env python3


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print("Which nth fibonacci number do you want?")
while True:
    try:
        number = int(input())
        if number < 0:
            raise ValueError
        break
    except ValueError:
        print("I really want a positive number!")

print("Number you are looking for is: " + str(fib(number)))
