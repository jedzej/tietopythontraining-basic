def collatz(number):

    if number % 2 == 0:
        new_number = number // 2

    else:
        new_number = 3 * number + 1
    if number == 1:
        raise SystemExit
    print(new_number)
    collatz(new_number)


print("enter an integer")
while True:
    try:
        input_number = int(input())
        break
    except:
        print("Please enter an integer")
collatz(input_number)
