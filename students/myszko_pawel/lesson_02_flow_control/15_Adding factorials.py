# Given an integer n, print the sum 1!+2!+3!+...+n!.
# This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

# Read an integer:
a = int(input())
# Print a value:
fctr = 1
suma = 1
# print(a)

for i in range (2, a+1):
    fctr *= i
    suma += fctr
print(suma)