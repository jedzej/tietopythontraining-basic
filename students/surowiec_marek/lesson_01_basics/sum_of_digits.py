# Read an 3 digits integer:
a = int(input())
# Print  the sum of its digits:
print(int(a%1000/100) + int(a%100/10) + a%10)
