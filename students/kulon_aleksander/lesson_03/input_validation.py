def collatz(number):
    tmp = number % 2
    if tmp:
        tmp = 3 * number + 1
        print(tmp)
        return tmp
    else:
        tmp = number // 2
        print(tmp)
        return tmp


print("Provide input")
try:
    number = int(input())
    while number != 1:
        number = collatz(number)
except ValueError:
    print("Must use an integer!")