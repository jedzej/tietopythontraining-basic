# Fibonacci: 1 1 2 3 5 8 13 ...
def fib(n):
    if isinstance(n, bool):
        raise TypeError("Wrong type.")

    if n <= 0:
        raise ValueError("The number must be greater than zero.")
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def validate_input():
    while True:
        n = int(input("Type a non-negative integer n: "))
        if n <= 0:
            print("The number must be greater than zero.")
            continue
        print("The nth Fibonacci number is:", fib(n))
        break


def main():
    while True:
        try:
            validate_input()
            break
        except ValueError:
            print("The number must be a non-negative integer.")


if __name__ == '__main__':
    main()
