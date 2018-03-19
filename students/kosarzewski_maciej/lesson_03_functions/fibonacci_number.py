def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print ("Enter number for Fibonacci sequence: ")
number = int(input())
print(fib(number))

