def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


try:
    number = int(input('Enter and integer: '))

except ValueError:
    print('Error: Invalid Value, the program should take in integers.')
    exit()

while number != 1:
    number = collatz(number)
    print(number)
