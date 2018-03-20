"""
Add try and except statements to the previous project to detect
whether the user types in a noninteger string. Normally, the int()
function will raise a ValueError error if it is passed a noninteger
string, as in int('puppy'). In the except clause, print a message
to the user saying they must enter an integer.
"""


def collatz(number):
    if number % 2 == 0:
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
while True:
    print("Plese input a positive integer:")
    try:
        value = int(input())
        if value > 0 and value % 1 == 0:
            break
    except ValueError:
        print("This is not an integer. Please try again.")

while True:
    value = collatz(value)
    if value == 1:
        break

# If input is 1, it is important to print info about finishing sequence.
print("End of collatz sequence")
