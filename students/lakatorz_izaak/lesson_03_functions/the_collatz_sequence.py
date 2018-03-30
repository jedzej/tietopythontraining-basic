# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this
# value. If number is odd, then should print and return 3 * number + 1.


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(str(result))
    return result


print("Enter number: ")
try:
    value = int(input())
    while value != 1:
        value = collatz(value)
except ValueError:
    print('You must enter an integer.')
