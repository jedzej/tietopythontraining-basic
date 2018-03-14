print("Input Validation\n")


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


while 1:
    try:
        number = int(input("Enter a number: "))
        if collatz(number) != 1:
            print(collatz(number))
        else:
            break
    except:
        print("You must enter an integer!\n")

print("The result of the Collatz Sequence is 1.\n\nThe program has ended.")
