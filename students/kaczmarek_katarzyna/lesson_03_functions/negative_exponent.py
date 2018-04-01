def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result


def validate_input():
    while True:
        a = float(input("Type a positive real number 'a': "))
        if a <= 0:
            print("Number 'a' must be positive. Try again.")
            continue
        n = int(input("Type an integer 'n' (power): "))
        print("The result is:", power(a, n))
        break


def main():
    while True:
        try:
            validate_input()
            break
        except ValueError:
            print("The first parameter 'a' must be a positive real number. "
                  "The second parameter 'n' must be an integer. " 
                  "Try again.")


if __name__ == '__main__':
    main()
