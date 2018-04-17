# For given integer n ≤ 9 print a ladder of n steps./
# The k-th step consists of the integers from 1 to k
# without spaces between them.

print('Give integer n <= 9')
n = int(input())

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(j, sep = ' ', end = '. ')
    print()
