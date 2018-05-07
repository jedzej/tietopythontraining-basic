"""
Statement
Given a positive real number a and integer n.
Compute an. Write a function power(a, n) to
calculate the results using the function and
print the result of the expression.

Don't use the same function from the standard library.
"""


def power(a, n):
    if (n < 0):
        return (1 / (a ** abs(n)))
    else:
        return a ** n


if __name__ == "__main__":
    try:
        print(power(float(input("Enter real number: ")),
                    float(input("Enter power number:"))))
    except ValueError:
        print("Error, invalid value.")
