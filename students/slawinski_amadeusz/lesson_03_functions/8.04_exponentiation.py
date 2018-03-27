#!/usr/bin/env python3


def power(a, n):
    if n:
        result = a * power(a, n - 1)
    else:
        result = 1
    return result


while True:
    try:
        print("Calculate a**n:")
        print("a = ", end='')
        a = float(input())
        if a < 0:
            print("a needs to be positive!")
            raise ValueError
        print("n = ", end='')
        n = int(input())
        if n < 0:
            print("n needs to be positive!")
            raise ValueError
        break
    except ValueError:
        print("Please try again!")

print(str(a) + "**" + str(n) + " = " + str(power(a, n)))
