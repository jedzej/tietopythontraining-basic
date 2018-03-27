# Program return a**n program using recursion.


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


try:
    a = int((input("a:")))
    n = int((input("n:")))

    result = power(a, n)

    print("a to power n is:", result)

except ValueError:
    print("It isn't integer!")
