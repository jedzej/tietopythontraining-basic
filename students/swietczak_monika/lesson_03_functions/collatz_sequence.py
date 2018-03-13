"""
Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
"""


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


a = int(input("Enter a number: "))
while a != 1:
    a = collatz(a)
