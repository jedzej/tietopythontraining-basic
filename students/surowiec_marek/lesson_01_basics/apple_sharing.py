# Read the numbers n students, k apples:
n = int(input())
k = int(input())
print(str(k//n) + ' apples will get each single student')
print(str(k%n) + ' apples will remain in the basket')