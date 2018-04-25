def collatz(number):

    if number % 2 == 0:
        number = number / 2
        print(int(number))
    else:
        number = 3 * number + 1
        print(int(number))

    return number


while True:
    n = input('number = ')

    try:
        n = int(n)
        break

    except ValueError:
        print('Enter an integer !!')
        continue

while n != 1:
    n = collatz(n)
