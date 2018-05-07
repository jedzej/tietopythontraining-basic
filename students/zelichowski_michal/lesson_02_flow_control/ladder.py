"""For given integer n ≤ 9 print a ladder of n steps. The k-th
step consists of the integers from 1 to k without spaces between them.

To do that, you can use the sep and end arguments for the function
print(). """

# Read an integer:
n = int(input())
# Print a value:
for k in range(1, n+1):
    for l in range(1, k+1):
        print(l, sep='', end='')
    print()
