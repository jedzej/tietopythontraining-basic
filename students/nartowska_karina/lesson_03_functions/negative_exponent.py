def power(a, n):
    print a ** n


def main():
    print("Enter a positive real number 'a' and integer 'n'")
    print("a is: ")
    a = float(input())
    print("n is: ")
    n = int(input())
    print("Result:")
    power(a, n)


main()
