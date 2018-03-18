def power(a, n):
    if n == 0:
        return 0
    elif n == 1:
        return a
    else:
        return a * power(a, n - 1)


def main():
    print("Enter a positive real number 'a' and a non-negative integer 'n'")
    print("a is: ")
    a = float(input())
    print("n is: ")
    n = int(input())
    print("Result:")
    print(power(a, n))


main()
