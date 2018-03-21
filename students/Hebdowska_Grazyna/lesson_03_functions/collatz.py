def collatz(number):
    if number == 0:
        return 1
    elif number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

try:
    N = int(input("N: "))
except ValueError:
    print("It wasn't number")

while N != 1:
    N = collatz(N)
    print(N)

