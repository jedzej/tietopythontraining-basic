# Read a 3-digit integer
a = int(input())
# Print the sum of its digits
print(a % 10 + a//10 % 10 + a//100)
