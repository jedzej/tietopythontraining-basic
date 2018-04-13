# Given a three-digit number. Find the sum of its digits.

a = int(input())

print( a//100 + (a%100)//10 + (a%10) )

