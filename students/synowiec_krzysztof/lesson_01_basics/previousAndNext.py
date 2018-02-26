
def main():
    inputNumber = int(input())
    previousNumber = inputNumber - 1
    nextNumber = inputNumber + 1

    print("The previous number for the number {0} is {1}.".format(inputNumber, previousNumber))
    print("The next number for the number {0} is {1}.".format(inputNumber, nextNumber))

if __name__ == '__main__':
    main()