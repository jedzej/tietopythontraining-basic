a to power n
#czy moge uzycz fabs?? co lepiej 2xfor czy if?
import math

def power(a, n):
    p = a
    if n != 0:
      if n < 0:
        n = int(math.fabs(n))
        for i in range(1, n):
          p = p * a
        p = 1 / p
      else:
        for i in range(1, n):
          p = p * a
    else:
      p = 1
    print ("a to power n is:", p)
    return p

try:
  a = int((input("a:")))
  n = int((input("n:")))
  
  power(a, n)
  
except ValueError:
   print("It isn't integer!")
