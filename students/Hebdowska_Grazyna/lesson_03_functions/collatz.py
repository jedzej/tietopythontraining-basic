def collatz(number):
    if number == 0:
        return 1
    elif number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


try:
    my_number = int(input("N: "))
except ValueError:
    print("It wasn't number")

while my_number != 1:
    my_number = collatz(my_number)
    print(my_number)
