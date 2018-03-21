print("The Collatz Sequence\n")


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


while 1:
    number = int(input("Enter a number: "))
    if collatz(number) != 1:
        print(collatz(number))
    else:
        break

print("The result of the Collatz Sequence is 1.\n\nThe program has ended.")
