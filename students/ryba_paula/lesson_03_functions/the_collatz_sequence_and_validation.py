def collatz(number):
    if number <= 0:
        raise ValueError
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def collatz_input_validation():
    number = int(input("Please type an integer: "))
    while number != 1:
        number = collatz(number)
        print(number)


while True:
    try:
        collatz_input_validation()
        break
    except ValueError:
        print("Input value must be a positive integer")
        continue
