def collatz(x):
    if x % 2 == 0:
        res = x // 2
    else:
        res = 3 * x + 1
    print(res)
    return res


while True:
    try:
        number = int(input("Enter a number: "))

        while number > 1:
            number = collatz(number)

    except ValueError:
        print('You must enter an integer!')
