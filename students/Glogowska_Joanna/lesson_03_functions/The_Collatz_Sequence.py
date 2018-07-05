def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    else:
        print(3 * number + 1)


collatz(int(input()))
