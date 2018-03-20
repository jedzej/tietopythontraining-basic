""""
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print
number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number
until the function returns the value 1.(Amazingly enough, this sequence actually works for any integer—sooner or later,
using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called
the Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the int() function; otherwise,
it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
"""


def collatz(value):
    try:
        print(int(value))
    except ValueError:
        print('ValueError: invalid literal for int().')
        print('Please enter an integer!')
        return None
    if value == 1:
        return None
    elif value % 2 == 0:
        return collatz(value >> 1)
    elif value % 2 == 1:
        return collatz(3 * value + 1)


starting_value = input()

collatz(starting_value)
