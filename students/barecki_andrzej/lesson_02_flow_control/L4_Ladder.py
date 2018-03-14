# For given integer n ≤ 9 print a ladder of n steps.
# The k-th step consists of the integers from 1 to k without spaces between them.
# To do that, you can use the sep and end arguments for the function print().

a = int(input())

index = 10 ** (a - 1)
result = 0
for x in range(1, a + 1):
    result += x * int(index)
    index /= 10

print(result)
