def fib(n):
    if n < 0:
        print("Error n cannot be less than 0")
        raise ValueError
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':


    print(fib(int(input())))
