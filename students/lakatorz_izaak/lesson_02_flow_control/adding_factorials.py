# Given an integer nn, print the sum 1!+2!+3!+...+n!1!+2!+3!+...+n!.

print("Enter integer")
n = int(input())

product = 1
sum_of_factorials = 0

for factor in range(1, n+1):
    product *= factor
    sum_of_factorials += product

print(sum_of_factorials)
