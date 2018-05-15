#Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.

import sys

def collatz(number):
    ret = 0
    if (number%2 == 0):
        ret = number // 2
    else:
        ret = 3* number + 1

    print(ret)
    return ret

print("Enter the number:")
try:
    n = int(input())
except ValueError:
    print("Error: Non-integer value entered, enter the integer value.")
    sys.exit()
collatz(n)

#2.

def collatz_1(num):
    res = collatz(num)
    if res == 1:
        return 1
    else:      
        return collatz_1(res)

print("Enter the number:")
try:
    n = int(input())
except ValueError:
    print("Error: Non-integer value entered, enter the integer value.")
    sys.exit()
collatz_1(n)
    
