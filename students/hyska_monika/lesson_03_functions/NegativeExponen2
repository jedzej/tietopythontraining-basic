# Program return a**n program using recursion, return value when n is negative
#import math

def power(a, n):
  if n != 0:
    if n < 0:
      #n = int(math.fabs(n))
      n = -1 * n
      a = a * power(a, n - 1)
      p = 1 / a
    else:
      a = a * power(a, n - 1)
      p = a
  else:
    p = 1
  return p

try:
  a = int((input("a:")))
  n = int((input("n:")))
 
  result = power(a, n)
  print ("a to power n is:", result)
 
except ValueError:
  print("It isn't integer!")
