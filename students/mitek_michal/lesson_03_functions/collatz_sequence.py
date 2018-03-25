
def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result)

        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)

        return result

    else:
        print("Wrong input :(")


def argument_input():
    global argument
    try:
        argument = int(input("Provide a number "))

    except ValueError:
        argument = None
        print("You must provide an integer, buddy ")


argument_input()

if __name__ == "__main__":
    while argument != 1 and argument is not None:
        argument = collatz(argument)
