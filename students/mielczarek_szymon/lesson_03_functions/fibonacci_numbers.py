def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def main():
    print(fib(int(input())))


if __name__ == "__main__":
    main()
