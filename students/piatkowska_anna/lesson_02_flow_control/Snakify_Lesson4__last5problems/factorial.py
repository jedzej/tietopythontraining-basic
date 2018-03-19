# Statement
# In mathematics, the factorial of an integer n, denoted by n!
# is the following product:
# n!=1×2×…×n
# For the given integer n calculate the value n!.
# Don't use math module in this exercise.


def my_factorial():
    print("Enter a number:")
    a = int(input())
    b = 1
    for i in range(1, a + 1):
        b *= i
    print(b)


if __name__ == '__main__':
    my_factorial()
