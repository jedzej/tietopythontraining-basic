def fib(n):
    if n <= 1 and n >= 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    number = int(input("Enter number for Fibonacci sequence: "))
    print(fib(number))
