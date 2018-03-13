# Add try and except statements to the previous project.


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(str(result))

    if result == 1:
        return 0
    else:
        collatz(result)


print('Enter number: ')
try:
    value = int(input())
    collatz(value)
except ValueError:
    print('You must enter an integer.')

