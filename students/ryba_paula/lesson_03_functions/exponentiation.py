def power(base, index):
    if index == 0:
        return 1
    elif index > 0:
        return base * power(base, index - 1)


def input_validation():
    while True:
        base = float(input("Pppppplease give the base number: "))
        if base < 0:
            print("Base number must be positive. Try again")
            continue
        index = int(input("Please give the power index: "))
        if index < 0:
            print("Power index must be non-negative. Try again")
            continue
        print("The result is:", power(base, index))
        break


while True:
    try:
        input_validation()
        break
    except ValueError:
        print("The first number must be real and the second int. Try again")
