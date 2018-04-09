# Fibonacci numbers
def fibonaczi(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonaczi(x - 2) + fibonaczi(x - 1)


def main():
    x = int(input())
    print(fibonaczi(x))


if __name__ == "__main__":
    main()
