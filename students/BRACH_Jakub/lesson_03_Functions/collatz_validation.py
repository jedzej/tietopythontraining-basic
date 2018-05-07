# Collatz Sequemce
def Collatz(number):
    if number % 2 == 0:
        retval = number // 2
    else:
        retval = 3 * number + 1
    print(retval)
    return retval


try:
    in_data = int(input())
    while in_data != 1:
        in_data = Collatz(in_data)
except ValueError:
    print("Error:Input must be integer!")
