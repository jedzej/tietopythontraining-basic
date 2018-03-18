# Fibonacci numbers
x = int(input())
def fibonaczi (x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonaczi(x-2) + fibonaczi(x-1)
print (fibonaczi(x))
