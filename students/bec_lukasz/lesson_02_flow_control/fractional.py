# Read an integer:
# a = int(input())
# Print a value:
# print(a)

n = int(input())
m = 1

for i in range(1, n + 1):
    m *= i

print(m)
