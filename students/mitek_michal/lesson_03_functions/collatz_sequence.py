
def collatz(number):

    if number % 2 == 0:
        result = number // 2

        return result

    else:
        result = 3 * number + 1

        return result


def argument_input():

    try:
        user_input = int(input("Provide a number "))
        return user_input

    except ValueError:
        print("You must provide an integer, buddy ")


if __name__ == "__main__":
    argument = argument_input()
    while argument != 1 and argument is not None:
        argument = collatz(argument)
