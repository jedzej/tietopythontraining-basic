#In mathematics, the factorial of an integer n, denoted by n! is the following #product:
#n!=1×2×…×n
#
#For the given integer n
#calculate the value n!. Don't use math module in this exercise. 

import sys

print("Enter the number:")
N = int(input())
if N < 0:
    print("Error: value less than 0")
    sys.exit()

f=1
if N == 0:
    print("Factorial:")
    print("1")
else:
    for i in range(1, N+1):
        f = f * i

print("Factorial:")
print(f)

