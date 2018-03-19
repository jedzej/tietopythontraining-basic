# Statement
# Given an integer n, print the sum 1!+2!+3!+...+n!.
# This problem has a solution with only one loop,
# so try to discover it. And don't use the math library :)


def adding_factorials():
    print("For given an integer n, the program will"
          " print the sum 1!+2!+3!+...+n!.")
    a = int(input("Enter a number n:"))
    sum_of_factorial = 0
    factorial = 1
    for i in range(1, a + 1):
        factorial = factorial * i
        sum_of_factorial += factorial
    print("The sum 1!+2!+3!+...+n! is:")
    print(sum_of_factorial)


if __name__ == '__main__':
    adding_factorials()
