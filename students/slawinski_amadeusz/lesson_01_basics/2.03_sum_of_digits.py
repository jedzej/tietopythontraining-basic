# given 3-digit nunber, print sum of its digits
n = int(input())

print((n // 100) + ((n // 10) % 10) + (n % 10))
