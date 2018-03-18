# For the given integer nn calculate the value n!n!. Don't use math module
# in this exercise.

print("Enter integer")
n = int(input())

product = 1

for factor in range(1, n+1):
    product *= factor

print(product)
