#!/usr/bin/env python3


def collatz(number):
    if number % 2:
        ret = 3 * number + 1
    else:
        ret = number // 2
    print(ret)
    return ret


while True:
    try:
        print("Enter number: ", end='')
        read_number = int(input())
        if read_number < 0:
            print("Please try again with positive number!")
        else:
            break
    except ValueError:
        print("Please try again with number!")


n = read_number
while n > 1:
    n = collatz(int(n))
