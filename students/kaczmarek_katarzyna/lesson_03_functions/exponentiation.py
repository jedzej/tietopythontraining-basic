def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


def validate_input():
    while True:
        a = float(input("Type a positive real number 'a': "))
        if a < 0:
            print("Number 'a' must be positive. Try again.")
            continue
        n = int(input("Type a non-negative integer 'n' (power): "))
        if n < 0:
            print("Number 'n' must be non-negative. Try again.")
            continue
        print("The result is:", power(a, n))
        break


def main():
    while True:
        try:
            validate_input()
            break
        except ValueError:
            print("The first parameter 'a' must be a positive real number. "
                  "The second parameter 'n' must be a non-negative integer. " 
                  "Try again.")


if __name__ == '__main__':
    main()
