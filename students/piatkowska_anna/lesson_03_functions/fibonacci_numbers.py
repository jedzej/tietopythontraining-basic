"""
Statement
Given a non-negative integer n, print the nth Fibonacci number.
 Do this by writing a function fib(n) which takes the non-negative
 integer n and returns the nth Fibonacci number.
Don't use loops, use the flair of recursion instead.
However, you should think about why the recursive
 method is much slower than using loops.
"""


def fib(n):
    if (n == 1):
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    try:
        print(fib(int(input("Enter integer > 0: "))))
    except ValueError:
        print("Entered value should be an integer.")
