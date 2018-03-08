def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        integer = int(input('Integer: '))
    except ValueError:
        print('Invalid integer')
    else:
        break

x = collatz(integer)
while x != 1:
    x = collatz(x)
