def collatz(number):
    if number <= 0:
        raise ValueError
    elif number % 2 == 0:
        half_even = number / 2
        print (half_even)
        return half_even
    elif number % 2 == 1:
        some_odd = (3 * number) + 1
        print (some_odd)
        return some_odd


def collatz_loop():
    print ("Please enter a number, positive, integer: ")
    value = int(input())
    while value != 1:
        value = collatz(value)


try:
    collatz_loop()
except ValueError:
    print('Not integer?')
