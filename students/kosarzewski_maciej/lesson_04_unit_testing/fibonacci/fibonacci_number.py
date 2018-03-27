def fib(n):
    if n <= 1 and n >= 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print("Enter number for Fibonacci sequence: ")
    number = int(input())
    print(fib(number))
