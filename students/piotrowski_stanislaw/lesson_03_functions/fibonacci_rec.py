# https://snakify.org/lessons/functions/problems/fibonacci_rec/
# piotrsta

n = float(input())

def fib(n):
    if n == 2 or n ==1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))
