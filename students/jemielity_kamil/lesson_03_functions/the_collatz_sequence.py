def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


integer = int(input('Integer: '))
x = collatz(integer)
while x != 1:
    x = collatz(x)
