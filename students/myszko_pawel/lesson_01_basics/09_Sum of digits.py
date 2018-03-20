# Given a three-digit number. Find the sum of its digits.

# Read an integer:
a = int(input())
# Print a value:
print( (a//100) + ((a%100))//10 + (a%10) )

