def get_collatz_nr(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def run(n):
    while n > 1:
        n = get_collatz_nr(n)
        print(n)


if __name__ == '__main__':
    try:
        n = abs(int(input()))
        run(n)
    except ValueError:
        print("Please enter integer!!!")
