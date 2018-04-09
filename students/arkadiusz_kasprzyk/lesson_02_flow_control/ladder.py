"""
description:
    For given integer n ≤ 9 print a ladder of n steps.
    The k-th step consists of the integers from 1 to k without spaces between them.
    To do that, you can use the sep and end arguments for the function print().
"""

print("""
    For given integer n ≤ 9 prints a ladder of n steps. 
    The k-th step consists of the integers from 1 to k without spaces between them.
""")

n = int(input("n = "))

step = ""

if n > 0 and n <= 9:
    for k in range(1, n+1):
        step += str(k)
        print(step)
else:
    print("n is too large; should be between 1 and 9.")
