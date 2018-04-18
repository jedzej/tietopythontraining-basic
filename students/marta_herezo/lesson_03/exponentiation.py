# Given a positive real number a and a non-negative integer n. Calculate a^n use recursion and the relation //
# an=a⋅a^(n−1). Print the result from the function power(a, n)

def power(a, n):
    if n < 0:
        a = 1 / a
        n = - n
        return power(a, n)
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return 1

a = float(input("Give a: "))
n = int(input("Give n: "))

print('Result of a^n is: ' + str(float(power(a, n))))