def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
