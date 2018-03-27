def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


try:
    n = int(input('Take me number: '))
    while n != 1:
        n = collatz(n)
        print(n)
except ValueError:
    print('Error: I need integer, not string')
