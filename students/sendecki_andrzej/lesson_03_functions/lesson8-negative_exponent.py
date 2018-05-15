#Given a positive real number a and integer n.
#Compute a^n. Write a function power(a, n) to calculate the results using the function and print the result of the expression.
#Don't use the same function from the standard library.  

import sys

def power(a, n):
    ret = a
    if (n == 0):
        return 1
    for i in range(1, n):
        ret = ret * a

    return ret

print("Enter real:")
a = float(input())
if (a <= 0):
    print("Error: non-positive number entered.")
    sys.exit()

print("Enter integer:")
n = int(input())

print(power(a, n))
