print("Input Validation\n")


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def loop():
    x = int(input("Enter a number: "))
    while x != 1:
        print(collatz(x))
        x = collatz(x)


try:
    loop()
except ValueError:
    print("You must enter an integer!\n")
