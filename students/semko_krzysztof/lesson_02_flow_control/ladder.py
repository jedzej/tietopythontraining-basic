"""
For given integer n ≤ 9 print a ladder of n steps.
The k-th step consists of the integers from 1 to k without spaces between them.

To do that, you can use the sep and end arguments for the function print().
"""

print("Please input an integer smaller then 9:")
number = int(input())
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(str(j), sep='', end='')
    print()
