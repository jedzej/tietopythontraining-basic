def collatz(number):
    """Calculates and prints the next element of Collatz sequence"""
    if number % 2 == 0:
        number //= 2
    else:
        number = number * 3 + 1
    print(number)
    return number


def main():
    number = 0
    # read integer from user until it is positive
    while number < 1:
        print("Enter positive integer: ", sep="", end="")
        try:
            number = int(input())
        except ValueError:
            print("Please enter an integer!")
            continue
        if number < 1:
            print("The number must be positive!")

    # calculate Collatz sequence until function calculating next element
    # returns 1
    number = collatz(number)
    while number != 1:
        number = collatz(number)


if __name__ == '__main__':
    main()
