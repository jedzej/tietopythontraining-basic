#Given an integer n, print the sum 1!+2!+3!+...+n!.
#
#This problem has a solution with only one loop, so try to discover it. And don't #use the math library :) 

import sys

print("Enter the number:")
N = int(input())
if N < 0:
    print("Error: value less than 0")
    sys.exit()

f=1
f_sum=0
if N == 0:
    print("1")
else:
    for i in range(1, N+1):
        f = f * i
        f_sum = f_sum + f

print("sum of factorials:")
print(f_sum)

