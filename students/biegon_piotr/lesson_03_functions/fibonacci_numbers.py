print("Fibonacci numbers\n")


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


n = int(input("Enter a non-negative integer: "))

print("\nThe {:d} number of Fibonacci sequence is: {:d}".format(n, fib(n)))
