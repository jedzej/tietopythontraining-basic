# For given integer n ≤ 9 print a ladder of n steps.
# The k-th step consists of the integers from 1 to k without spaces between them.
# To do that, you can use the sep and end arguments for the function print().

# Read an integer:
a = int(input())
# Print a value:
for i in range(1, a+1):
    for k in  range(1, i+1):
        print(k, sep='', end='')
    print()