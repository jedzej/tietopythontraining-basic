"""
Add try and except statements to the previous project to detect
whether the user types in a noninteger string. Normally, the int()
function will raise a ValueError error if it is passed a noninteger
string, as in int('puppy'). In the except clause, print a message
to the user saying they must enter an integer.
"""


def collatz(number):
    if number <= 0:
        print("This is not a positive integer.")
        return -1
    elif number % 2 == 0:
        result = number // 2
        print(str(result))
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print(str(result))
        return result
    else:
        print("This is not a positive integer.")
        return -1


value = -1
while value != 1:
    try:
        if value == -1:
            print("Please input a number:")
            value = float(input())
        else:
            value = collatz(value)
    except ValueError:
        print("This is not a number. Please try again.")

# If input is 1, it is important to print info about finishing sequence.
print("End of collatz sequence")
