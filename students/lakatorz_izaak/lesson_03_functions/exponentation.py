# Given a positive real number a and a non-negative integer n. Calculate an
# without using loops, ** operator or the built in function math.pow().
# Instead, use recursion and the relation an=a⋅an−1


def exponentation(a, n):
    if n == 0:
        return 1
    else:
        return a*exponentation(a, n-1)


print("Enter base (a):")
base = float(input())

print("Enter exponent (n):")
exponent = int(input())

print(exponentation(base, exponent))
