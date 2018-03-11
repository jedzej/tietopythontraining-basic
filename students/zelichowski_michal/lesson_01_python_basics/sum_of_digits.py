# Given a three-digit number. Find the sum of its digits.

a = int(input())
b = a // 100
c = (a // 10) % 10
d = a % 10
print(b + c + d)

