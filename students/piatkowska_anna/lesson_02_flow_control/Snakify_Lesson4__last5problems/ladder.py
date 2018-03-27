# Statement
# For given integer n ≤ 9 print a ladder of n steps.
# The k-th step consists of the integers from 1 to k without
# spaces between them.
# To do that, you can use the sep and end arguments for
# the function print().


def ladder():
    print("Enter number between 1-9:")
    a = int(input())
    rung = ""
    for i in range(1, a + 1):
        rung = rung + str(i)
        print(rung)


if __name__ == '__main__':
    ladder()
