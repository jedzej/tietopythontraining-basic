def collatz(number):
    print(number)

    if number == 1:
        print("Koniec")
    elif number % 2 == 0:
        collatz(number // 2)
    else:
        collatz(3 * number + 1)


try:
    collatz(int(input()))
except ValueError:
    print("To nie liczba!")
