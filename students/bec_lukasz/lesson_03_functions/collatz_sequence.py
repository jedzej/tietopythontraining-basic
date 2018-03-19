

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


def take_number():
    print('Type an integer')
    number = int(input())

    result = collatz(number)

    while result != 1:
        number = collatz(result)
        result = collatz(number)


try:
    take_number()
except ValueError:
    print('Only integers accepted')
