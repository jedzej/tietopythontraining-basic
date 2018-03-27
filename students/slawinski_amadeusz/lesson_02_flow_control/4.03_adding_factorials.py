# prints sum of factorials from 1! to n!

n = int(input())

sum_of_factorial = 1

for i in range(n, 1, -1):
    sum_of_factorial = sum_of_factorial * i + 1

print(sum_of_factorial)
