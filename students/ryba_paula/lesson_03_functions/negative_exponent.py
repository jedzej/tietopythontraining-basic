def power(base, index):
    return base ** index


def input_validation():
    while True:
        base = float(input("Please give the base number: "))
        if base <= 0:
            print("The base number must be positive")
            continue
        index = int(input("Please give a power index: "))
        print("The result is:", power(base, index))
        break


while True:
    try:
        input_validation()
        break
    except ValueError:
        print("The first number must be real and the second integer")
