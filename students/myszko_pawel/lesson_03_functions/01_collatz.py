# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return
# this value. If number is odd, then collatz() should print and return
# 3 * number + 1.
# Then write a program that lets the user type in an integer and that
# keeps calling collatz() on that number until the function returns
# the value 1.


def collatz(num_1):
    if num_1 % 2 == 0:
        num_1 = num_1 // 2
        print(num_1)
        return int(num_1)
    elif num_1 % 2 == 1:
        num_1 = 3 * num_1 + 1
        print(num_1)
        return int(num_1)


try:
    number = int(input("Please type the number (collatz() function "
                       "parameters:"))
    while number != 1:
        number = collatz(number)
except ValueError:
    print("Please type an intiger")
