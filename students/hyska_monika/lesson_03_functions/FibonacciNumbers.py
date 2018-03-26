# Program return a**n program using recursion, return value when n is negative

def fib(n):
  if n == 0:
    return 0 
  elif n == 1:
    return 1
  else:
    return (fib(n - 1) + fib(n - 2))
  return n

try:
  n = int((input("Put n (non-negative):")))
 
  result = fib( n)
  print ("Fibonacci is:", result)
 
except ValueError:
  print("It isn't integer!")
