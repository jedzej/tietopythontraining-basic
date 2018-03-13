def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


number = int(input())
while number != 1:
    number = collatz(number)
    print(number)



