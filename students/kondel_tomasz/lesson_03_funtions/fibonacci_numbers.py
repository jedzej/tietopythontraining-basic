def fib(n_string):
    try:
        n = int(n_string)
    except ValueError:
        print('Please type int value')
        return None

    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    n_string = input()
    result = fib(n_string)
    print(result)


if __name__ == '__main__':
    main()
