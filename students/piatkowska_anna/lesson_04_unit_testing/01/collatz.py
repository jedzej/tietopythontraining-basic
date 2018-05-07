"""
Write a function named collatz() that has one parameter named number
If number is even, then collatz() should print number // 2 and
return this value. If number is odd, then collatz()
should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.
Amazingly enough, this sequence actually works for any integer—sooner
or later, using this sequence, you’ll arrive at 1! Even mathematicians
aren’t sure why. Your program is exploring what’s called the Collatz
sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the
int() function; otherwise, it will be a string value.

Hint: An integer number is even if number % 2 == 0,
and it’s odd if number % 2 == 1.

The output of this program could look something like this:


Enter number:
3
10
5
16
8
4
2
1
"""


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        print(3 * number + 1)
        return(3 * number + 1)


if __name__ == "__main__":
    a = int(input("Enter an integer: "))
    while a != 1:
        a = collatz(a)
