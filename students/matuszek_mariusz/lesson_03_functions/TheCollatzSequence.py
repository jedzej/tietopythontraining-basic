def collatz(number):

    if number % 2 == 0:
        number = number / 2
        print(int(number))
    else:
        number = 3 * number + 1
        print(int(number))

    return number


n = int(input('number = '))

while n != 1:
    n = collatz(n)
