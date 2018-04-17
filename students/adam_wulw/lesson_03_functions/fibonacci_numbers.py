def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


num_in = int(input('Enter number\n'))
print(fib(num_in))
