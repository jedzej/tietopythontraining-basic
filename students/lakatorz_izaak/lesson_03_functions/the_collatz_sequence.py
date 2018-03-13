# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this
# value. If number is odd, then should print and return 3 * number + 1.


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(str(result))

    if result == 1:
        return 0
    else:
        collatz(result)


print("Enter number: ")
value = int(input())

collatz(value)
