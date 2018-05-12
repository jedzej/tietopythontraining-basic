#Test your code from Fibonacci numbers from previous lesson. You can use pytest or unittest.

import sys

def fib(n):
   if (n <= 1):
       return n
   else:
       return(fib(n-1) + fib(n-2))

def test_fib_zero_and_one():
    assert fib(0) == 0
    assert fib(1) == 1

def test_fib_greater_than_one():
    assert fib(2) == 1
    assert fib(10) == 55

def test_fib_less_than_zero():
    # In ideal world an exception should be raised
    # but it was not defined in the lessons' scope.
    # Thus returning the negative here is correct.
    assert fib(-2) == -2
    assert fib(-3) == -3

print("Enter non-negative integer:")
# Replaced input for the pytest's sake
#a = int(input())
a = 4
if (a < 0):
    print("Error: negative number entered.")
    sys.exit()

print(fib(a))
