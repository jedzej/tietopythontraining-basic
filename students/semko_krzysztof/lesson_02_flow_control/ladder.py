"""
For given integer n ≤ 9 print a ladder of n steps.
The k-th step consists of the integers from 1 to k without spaces between them.

To do that, you can use the sep and end arguments for the function print().
"""

print("Please input an integer smaller then 9:")
number = int(input())
line = ""
for i in range(1, number + 1):
    line += str(i)
    print(line, sep='')
